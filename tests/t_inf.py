from holytools.configs import FileConfigs
from holytools.devtools import Unittest

from data.providers import ContextProvider
from pdfquery.inference import InferenceModule, GroqInf, OllamaInf
from pdfquery.language import Context


# --------------------------------------------------

class TestInference(Unittest):
    @classmethod
    def setUpClass(cls):
        credentials = FileConfigs.credentials()
        context_provider = ContextProvider()
        cls.groq_api_key : str = credentials.get(key='groq_api_key')
        paper_context : Context = context_provider.get_graphite_paper_context()
        query = Context.singleton(content=f'Please quote an equation from the above provided text')
        cls.paper_equation_query : Context = paper_context + query

        magna_carta_summary = Context.singleton(content=f"""Magna Carta Libertatum (Medieval Latin for "Great Charter of Freedoms"), commonly called Magna Carta or sometimes Magna Charta ("Great Charter"),[a] is a royal charter[4][5] of rights agreed to by King John of England at Runnymede, near Windsor, on 15 June 1215.[b] First drafted by the Archbishop of Canterbury, Cardinal Stephen Langton, to make peace between the unpopular king and a group of rebel barons who demanded that the King confirm the Charter of Liberties, it promised the protection of church rights, protection for the barons from illegal imprisonment, access to swift and impartial justice, and limitations on feudal payments to the Crown, to be implemented through a council of 25 barons. Neither side stood by their commitments, and the charter was annulled by Pope Innocent III, leading to the First Barons' War.""")

        repetition_query = Context.singleton(content=f'Please repeat the above message in its entirety')
        cls.magna_carta_repetion_query : Context = magna_carta_summary + repetition_query

    def test_groq_inf(self):
        inf_module = GroqInf(api_key=self.groq_api_key)
        self.check_queries(inf_module)

    def test_ollama_inf(self):
        inf_module = OllamaInf()
        self.check_queries(inf_module=inf_module)

    # ------------------------------------------------------------------

    def check_queries(self, inf_module : InferenceModule):
        repetition_response = inf_module.get_response_text(context=self.magna_carta_repetion_query)
        self.assertIn('Magna Carta Libertatum', repetition_response)

        paperquery_response = inf_module.get_response_text(context=self.paper_equation_query)
        print(f'Response = {paperquery_response}')
        self.assertIsInstance(paperquery_response, str)


if __name__ == "__main__":
    TestInference.execute_all()