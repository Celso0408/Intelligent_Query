from __future__ import annotations

from abc import abstractmethod
from typing import Optional

from  pdfquery.language.context import Context

# -------------------------------------------------

class InferenceModule:
    def query_routine(self, context : Context, model : Optional[str] = None):
        """Converses with the user until routine is exited"""
        while True:
            user_query = input("User:")
            if user_query == 'exit':
                print(f'Exiting query routine')
                break
            context += Context.singleton(content=user_query)
            response = self.get_response_text(context, model)
            print(f'Assistant : {response}')
            context += Context.singleton(content=response, role='assistant')

    @abstractmethod
    def get_response_text(self, context : Context, model : Optional[str] = None) -> str:
        """Generates and returns response to the current context"""
        pass

    @abstractmethod
    def get_default_model(self) -> str:
        """Model used if no model is specified"""
        pass