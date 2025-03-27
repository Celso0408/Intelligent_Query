import json
from typing import Optional

import json_repair
from holytools.configs import FileConfigs

from data.providers import ContextProvider
from pdfquery.inference.groq_inf import GroqInf
from pdfquery.inference.inf import InferenceModule
from pdfquery.language import Context

# --------------------------------------------------------

class GraphitePaperEval:
    def __init__(self, inf_module : InferenceModule):
        self.inf_module : InferenceModule = inf_module

    def question_routine(self, context: Context, model: Optional[str] = None):
        """Question routine on basic papers on the graphite paper (paperID = phys1)"""
        q1 = f'Who are the authors of the paper?'
        # q2 = (f'Can you cite a formula for how to compute the bulk modulus from the elastic constant? '
        #       f'Give the number of the equation')
        q3 = (f'What bulk properties of graphite are of interest in this paper? Name all'
              f'releveant physical quantities that the paper cites. Group them sensibly.')
        q4 = (f'What reference does the paper cite for the experimental values? '
              f'For each reference present a link if possible and show what values they give for the quantities')
        # q6 = (f'What is the best performing correction scheme according to this paper? Cite passages or values from the paper'
        #     f'that argue for or confirm this.')

        for q in [q1, q3, q4, q4]:
            context += Context.singleton(content=q)
            print(f'[User]: {q}')
            response = self.inf_module.get_response_text(context=context, model=model)
            print(f'[Assistant]: {response}')
            context += Context.singleton(content=response, role='assistant')

    def table_value_extraction(self, paper_context: Context):
        """Launches a routine for the extraction of numberical quantities from a table in the paper"""
        approaches = ['PBE', 'PBE + TS + SCS', 'DF1', 'PBE + TS + SCS + MBD', 'VV10', 'vdW-DF', 'C09 (vdw)']
        extracted_json = self.extract_value_json(paper_context=paper_context, approaches=approaches)
        print(f'- Extracted json data:\n{extracted_json}')

        gt_json = self.get_gt_json()
        gt_json = self.cast_to_lower(gt_json)
        print(f'- Ground truth json data for comparison:\n{gt_json}')

        total_queries = 0
        no_mismatches = 0

        print(f'-------------------- Results ----------------------------')
        for m1, m2 in zip(extracted_json.keys(), gt_json.keys()):
            for attr in gt_json[m1]:
                total_queries += 1
                try:
                    gt_val = gt_json[m1][attr]
                    val = extracted_json[m1][attr]
                    if val == "":
                        val = None
                    if val != gt_val and val != -gt_val:
                        print(f'Mismatch for method {m1} and property {attr}: {val} != {gt_val}')
                        no_mismatches += 1
                except:
                    print(f'Missing attribute {attr} for method {m1}')
                    no_mismatches += 1

        print()
        print(f'-------------------- Summary ----------------------------')
        print(f'- Total queries                    : {total_queries}')
        print(f'- Number of mismatches or undefined: {no_mismatches}')
        print(f'Error ratio = {(no_mismatches / total_queries)*100}%')


    def extract_value_json(self, paper_context : Context, approaches : list[str], use_quotation : bool = False, use_error_checking=True):
        intro = ('This paper includes information on the bulk properties of graphite. Among the properties discussed are'
                  'the equilibrium lattice parameters \"a0\" \"c0\", bulk modulus \"B0\", the first deriviate of the bulk modulus \"B\'0\",'
                  f'the curvature \"C33\" and curvature deriviate \"C333\" of the interlayer binding energy, the cohesive energy \"Ecoh\" '
                  f'and the interlayer binding energy \"Eb\".'
                  f'For each of the mentioned properties you will extract the values according to following approaches'
                  f'{approaches}.')
        json_extraction_query = ('Now please extract the values for a0, c0, B0, B\'0, C33, C333, Ecoh and Eb as json data as follows: {[method] : {[propertyA]} : [valueA], [propertyB] : [valueB]}'
                 'Please be sure to output only the json as the result will be parsed automatically. Do not put it in a markdown code block'
                  'If a value is absent use null')



        if use_quotation:
            method = (f'To do this first quote all relevant lines literally from the document'
                      f'In the future you will be asked to extract values only from this quoted material')
            q1 = intro + method
            initial_context = paper_context + Context.singleton(content=q1)
            print(f'[User]: {q1}')
            response = self.inf_module.get_response_text(context=initial_context)
            print(f'Assistant: {response}')

            c2 = initial_context
            c2 += Context.singleton(content=f'Quoted content: {response}', role='assistant')
            c2 += Context.singleton(content=json_extraction_query)
            r = self.inf_module.get_response_text(context=c2)

        else:
            c = paper_context + Context.singleton(content=intro+json_extraction_query)
            r = self.inf_module.get_response_text(context=c)
            print(f'Initially produced json = {r}')

        if use_error_checking:
            correction_request = ('Now carefully check and correct for any mistakes in the original json data detailing the value information'
                                  f'Only extract data for the approaches {approaches}, do not add any new approaches'
                                  'Please be sure to output only the json as the result will be parsed automatically. Do not put it in a markdown code block'
                                  'If a value is absent use null.')
            c = (Context.singleton(intro) + Context.singleton(json_extraction_query)
                 + paper_context + Context.singleton(content=r) + Context.singleton(content=correction_request))
            r = self.inf_module.get_response_text(context=c)

        print(f'Final json response = {r}')
        r = json_repair.repair_json(r)
        json_dict = json.loads(r)
        json_dict = self.cast_to_lower(json_dict)

        return json_dict

    @staticmethod
    def get_gt_json() -> dict:
        gt_json = {"PBE": {
        "a0": 2.466,
        "c0": 8.755,
        "B0": 1.6,
        "B'0": 15.7,
        "C33": 0.55,
        "C333": -4,
        "Ecoh": -7.85,
        "Eb": -1.2,
        },
        "PBE + TS + SCS": {
        "a0": 2.461,
        "c0": 6.633,
        "B0": 40.5,
        "B'0": 12.77,
        "C33": 26.79,
        "C333": -184,
        "Ecoh": -7.97,
        "Eb": -53.76,
        },
        "DF1": {
        "a0": 2.46,
        "c0": 7.199,
        "B0": None,
        "B'0": None,
        "C33": 23,
        "C333": None,
        "Ecoh": None,
        "Eb": -18.90,
        },
        "PBE + TS + SCS + MBD": {
        "a0": 2.46,
        "c0": 6.70,
        "B0": None,
        "B'0": None,
        "C33": None,
        "C333": None,
        "Ecoh": None,
        "Eb": -48,
        },
        "VV10": {
        "a0": 2.46,
        "c0": 6.777,
        "B0": None,
        "B'0": None,
        "C33": 46.1,
        "C333": None,
        "Ecoh": None,
        "Eb": -27.07,
        },
        "vdW-DF": {
        "a0": 2.47,
        "c0": 7.52,
        "B0": 12,
        "B'0": None,
        "C33": 13,
        "C333": None,
        "Ecoh": None,
        "Eb": -24,
        },
        "C09 (vdw)": {
        "a0": 2.47,
        "c0": 6.54,
        "B0": None,
        "B'0": None,
        "C33": None,
        "C333": None,
        "Ecoh": None,
        "Eb": -26.9,
        },
        "Experiment": {
        "a0": 2.462,
        "c0": 6.707,
        "B0": 35.6,
        "B'0": 8.9,
        "C33": 37.6,
        "C333": -530,
        "Ecoh": -7.37,
        "Eb": -48,
        }
        }

        return gt_json


    @staticmethod
    def cast_to_lower(json_dict : dict) -> dict:
        lower_case_dict = {}
        for m in json_dict.keys():
            lowercase_substore = {attr.lower() : json_dict[m][attr] for attr in json_dict[m]}
            lower_case_dict[m] = lowercase_substore
        return lower_case_dict


if __name__ == "__main__":
    cred_configs = FileConfigs.credentials()
    groq_api_key = cred_configs.get(key='groq_api_key')

    ollama_inf = GroqInf(api_key=groq_api_key)
    evaluator = GraphitePaperEval(inf_module=ollama_inf)
    provider = ContextProvider()
    full_context = provider.get_graphite_paper_context()
    evaluator.table_value_extraction(paper_context=full_context)

