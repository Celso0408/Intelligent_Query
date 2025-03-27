from __future__ import annotations

import base64
from dataclasses import dataclass
from typing import Optional


@dataclass
class Message:
    text_content: str
    role: str = 'user'
    img_b64: Optional[str] = None

    @staticmethod
    def img_to_b64(img_fpath: str) -> str:
        with open(img_fpath, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        return encoded_string

    @classmethod
    def from_img(cls, msg : str, img_fpath : str):
        return cls(text_content=msg, img_b64=Message.img_to_b64(img_fpath=img_fpath))

    def as_groq(self) -> dict:
        """Converts the message to the format as required by groq"""
        if self.role == 'user':
            content = [{"type": "text", "text": self.text_content}]
        else:
            content = self.text_content
        if self.img_b64:
            url = f'data:image/jpeg;base64,{self.img_b64}'
            content.append({"type": "image_url", "image_url": {"url": url}})

        return {'role': self.role, 'content': content}

    def as_ollama(self) -> dict:
        """Converts the message to the format as required by Ollama"""
        msg_dict = {'role' : self.role, 'content' : self.text_content}
        if self.img_b64:
            msg_dict['images'] = self.img_b64
        return msg_dict
