import json

from data.providers import ContextProvider, FileProvider
from pdfquery.inference import InferenceModule
from pdfquery.inference.ollama_inf import OllamaInf
from pdfquery.language import Context


# -----------------------------------------

class SPIQA:
    def __init__(self, inf_module : InferenceModule):
        self.data_provider : FileProvider = FileProvider()
        self.context_provider : ContextProvider = ContextProvider()
        self.inf_module: InferenceModule = inf_module
        with open(self.data_provider.spiqa_jsonA_fpath, 'r') as f:
            self.testA_metadata : dict = json.loads(f.read())

    def paper_qa(self, num_papers : int = 10):
        paper_ids = list(self.testA_metadata.keys())
        for N, pid in enumerate(paper_ids[:num_papers]):
            paper = self.testA_metadata[pid]
            metadata = paper['qa'][0]
            question = metadata['question']
            context = self.context_provider.get_context(pid=pid)
            context += Context.singleton(content=question)

            model_answer = self.inf_module.get_response_text(context=context)
            correct_answer = metadata['answer']
            print(f'({N}):  https://arxiv.org/pdf/{pid}')
            print(f'Q: {question}')
            print(f'A1 (Model)       : {model_answer}')
            print(f'A2 (Ground truth): {correct_answer}\n')


    def show(self):
        for N, pid in enumerate(self.testA_metadata):
            paper = self.testA_metadata[pid]
            metadata = paper['qa']
            print(f'({N}): https://arxiv.org/pdf/{pid}')
            print(f'Q: {metadata[0]["question"]}')
            print(f'A: {metadata[0]["answer"]}')
            print(f'Context: {paper["all_figures"]}')
            print()

if __name__ == "__main__":
    # from holytools.configs import FileConfigs
    # creds = FileConfigs.credentials()
    # api_key = creds.get(key='groq_api_key')
    #
    # inf_model = OllamaInf()
    # spiqa = SPIQA(inf_module=inf_model)
    # spiqa.paper_qa(num_papers=10)

    spiqa = SPIQA(inf_module=OllamaInf())
    spiqa.show()