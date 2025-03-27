from typing import Optional

import ollama

from pdfquery.inference.inf import InferenceModule
from pdfquery.language import Context

# -------------------------------------------------

class OllamaInf(InferenceModule):
    def get_response_text(self, context: Context, model : Optional[str] = None) -> str:
        if model is None:
            model = self.get_default_model()
        response = ollama.chat(
            messages=[msg.as_ollama() for msg in context],
            options={'num_ctx' : 2**14},
            model=model)
        return response['message']['content']

    def get_default_model(self) -> str:
        return 'llama3.2:3b'
