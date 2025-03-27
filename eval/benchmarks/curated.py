import json
import os.path
import threading

from holytools.configs import FileConfigs

from data.providers import ContextProvider, DocType, FileProvider
from pdfquery.inference import InferenceModule
from pdfquery.inference.groq_inf import GroqInf
from pdfquery.language import Context
from pdfquery.prompts.provider import PromptProvider

# --------------------------------------------------------------------------

class CuratedEval:
    def __init__(self, inf_module : InferenceModule):
        self.inf_module : InferenceModule = inf_module
        self.context_provider : ContextProvider = ContextProvider()
        self.file_provider : FileProvider = self.context_provider.file_provider
        data_dirpath = self.context_provider.file_provider.data_dirpath

        qa_fpath = os.path.join(data_dirpath,'curated', 'qa.json')
        with open(qa_fpath, 'r') as f:
            content = f.read()
            self.qa : dict = json.loads(content)
        self.prompt_provider = PromptProvider(fname='prompts.txt')
        self.conv_history : str = ''

    def evaluate(self, paper_ids : list[str], doc_type : DocType):
        """Evalutes Q&A routine on papers specified by paper_ids"""
        for pid in paper_ids:
            pid = pid.replace('.pdf', '')
            print(f'- Processing {pid}')

            for task in ['select', 'list', 'find']:
                successes = self.get_successes(pid=pid, task=task, reps=4, doctype=doc_type)
                signs = ['✓' if s else '❌' for s in successes]
                print(f'    - {task}: {signs}')

            print()

    def get_successes(self, pid : str, task : str, reps : int, doctype : DocType):
        """Retrieves a list of successes/failures the task for paper specified by paperID pid. The task is repeates [rep] number of times"""
        successes = []
        for _,j in [(i, j) for i in range(reps) for j in [1, 2]]:
            paper_question = self.qa[pid][f'q{task}{j}'] + 'The result will be processed automatically'

            model_answer = self.query(pid=pid, question=paper_question, doctype=doctype)
            model_parts = self.extract_model_parts(answer=model_answer)

            gt_answer = self.qa[pid][f'a{task}']
            gt_part_list = self.extract_gt_options_sets(answer=gt_answer)

            print(f'Model parts = {model_parts}')
            print(f'GT parts = {gt_part_list}')
            successes.append(self.matches_option(model_parts, gt_part_list))

        return successes

    def query(self, pid : str, question : str, doctype : DocType) -> str:
        """Queries a model a question [question] on paper specified by paperID [pid], executes the COT routine and returns the answers"""
        paper_context = self.context_provider.get_context(pid=pid, doctype=doctype)
        initial_query = self.prompt_provider.retrieve(name='query')
        query_context = Context.singleton(content=f'{initial_query} {question}')
        c1 = paper_context + query_context
        r1 = self.inf_module.get_response_text(context=c1)

        response_context = Context.singleton(content=r1, role='assistant')
        refinment_context = Context.singleton(content=self.prompt_provider.retrieve(name='refinement'))
        c2 = c1 + response_context + refinment_context
        r2 = self.inf_module.get_response_text(context=c2)

        # The current versino includes 2 review cycles, but this review cycle i.e. the second review cycle has not yielded a noticable improvement to the point
        # where I am not sure it did anything positive at all. The commented code below (declaring c3, r3) could be cut at your discretion
        # c3 = c2 + Context.singleton(content=f'Since the result is very important, perform a final check. '
        #                                     f'Convince yourself of the accuracy of your response, then give your final answer in the last line of your response.'
        #                                     f'The result will again be parsed automatically.')
        # r3 = self.inf_module.get_response_text(context=c3)


        self.conv_history += f'Q: {question}\n'
        self.conv_history += f'A11: {r1}\n'
        self.conv_history += f'A12: {r2}\n'

        return r2

    @staticmethod
    def extract_model_parts(answer : str) -> set[str]:
        """The model answer is broken up into a set of required parts delimited by ,"""
        last_line = answer.split('\n')[-1]
        model_parts = last_line.split(',')
        model_parts = {p.strip().lower() for p in model_parts}
        return model_parts

    @staticmethod
    def extract_gt_options_sets(answer : str) -> list[set[str]]:
        """The gt answer is broken up into a set of required parts"""
        gt_options = answer.split(' | ')
        gt_part_list = []
        for o in gt_options:
            gt_parts = set(o.split(','))
            gt_parts = {p.strip().lower() for p in gt_parts}
            gt_part_list.append(gt_parts)
        return gt_part_list

    @staticmethod
    def matches_option(model_parts : set[str], gt_part_list : list[set[str]]) -> bool:
        for parts in gt_part_list:
            if model_parts == parts:
                return True
        return False


if __name__ == "__main__":
    credentials = FileConfigs.credentials()
    groq_inf = GroqInf(api_key=credentials.get(key='groq_api_key'))
    paper_eval = CuratedEval(inf_module=groq_inf)
    all_pids = os.listdir(paper_eval.file_provider.curated_pdf_dirpath)
    paper_eval.evaluate(paper_ids=['phys1'], doc_type=DocType.MARKDOWN)

    print(f'+-----------------------------------------+')
    print(f'-> Conversation history ')
    print(paper_eval.conv_history)

    # test_pid = f'med1'
    # context_provider = ContextProvider()
    # test_context = context_provider.get_context(pid=test_pid, doctype=DocType.LATEX)
    # print(test_context)