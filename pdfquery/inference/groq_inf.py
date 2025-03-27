from __future__ import annotations

from typing import Optional
from groq import Groq


from pdfquery.language import Context
from .inf import InferenceModule

# -------------------------------------------------

class GroqInf(InferenceModule):
    def __init__(self, api_key : str):
        self.groq : Groq = Groq(api_key=api_key)

    def get_response_text(self, context : Context, model : Optional[str] = None) -> str:
        if model is None:
            model = self.get_default_model()
        response = self.groq.chat.completions.create(
            temperature=0,
            messages=[msg.as_groq() for msg in context],
            model=model)
        return response.choices[0].message.content

    def get_default_model(self) -> str:
        return 'llama-3.3-70b-versatile'
