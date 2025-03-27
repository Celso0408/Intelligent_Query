import requests
from holytools.configs import FileConfigs

# ------------------------------------------------------------------

class AccuracyRater:
    def __init__(self, api_key : str):
        self._api_key : str = api_key
        # Ground truth: [0.9, 0.9, 0.3, 0.2, 0]

        # MiniLM: [0.75, 0.78, 0.54, 0.41, -0.13]
        self._api_url : str = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
        # Stella: [0.71, 0.75, 0.74, 0.68, 0.48]
        #self._api_url : str = "https://api-inference.huggingface.co/models/dunzhang/stella_en_1.5B_v5"
        #GIST: [0.79, 0.86, 0.67, 0.6, 0.28]
        #self._api_url : str = "https://api-inference.huggingface.co/models/avsolatorio/GIST-large-Embedding-v0"

    def rate(self, source : str, others : list[str]) -> list[float]:
        """Rates how closely the 'other' inputs represent the 'source' input; Doesn't work well at the moment"""
        headers = {"Authorization": f"Bearer {self._api_key}"}
        payload = { "inputs": { "source_sentence": source, "sentences" : others}}
        response = requests.post(self._api_url, headers=headers, json=payload)
        print(response)
        return response.json()


if __name__ == "__main__":
    # eco_paper_correct_answer = "The Ridge method achieved the lowest sum of absolute percentage errors (136.84), indicating the highest tracking accuracy in terms of minimizing absolute deviations from the index. However, this doesn't necessarily translate to the best overall performance."
    # eco_paper_answers = [
    #     "The Ridge method achieved the highest tracking accuracy. The tracking accuracy is not the only metric to optimize but also the number of stocks traded",
    #     "The highest tracking accuracy was achieved by the Ridge method. But tracking accuracy is not the only relevant metric relevant for overall performance",
    #     "The Cluster method achieved the highest tracking accuracy. The tracking accuracy is not the only metric to optimize but also the number of stocks traded",
    #     "The tracking accuracy evaluates how closely the ETF replicates the index performance",
    #     "The mitochondria is the powerhouse of the cell"]

    with open(f'/home/daniel/sciai/pdfquery/data/curated/structured/med2/markdown.md') as f:
        ref_text = f.read()

    query = "World health organization"
    sentences = ref_text.split('\n')

    configs = FileConfigs.credentials()
    evaluator = AccuracyRater(api_key=configs.get(key='hf_api_key'))
    accuracies = evaluator.rate(source=query, others=sentences)
    accuracies = [round(d, 2) for d in accuracies]
    for acc, s in zip(accuracies, sentences):
        print(f'{acc} | {s}')