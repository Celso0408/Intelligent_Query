from __future__ import annotations
import os
import re

import tempfile

from pdfquery.language.message import Message
from pdfquery.pdfparser import PdfParser

# ---------------------------------------------

class Context(list[Message]):
    def to_str(self):
        total_str = ''
        for m in self:
            total_str += m.text_content
        return total_str

    @classmethod
    def empty(cls) -> Context:
        """Generates an empty context"""
        return Context()

    @classmethod
    def singleton(cls, content : str, role : str = 'user') -> Context:
        """Generates a context with a single message"""
        return Context([Message(text_content=content, role=role)])

    @classmethod
    def from_pdf(cls, pdf_fpath : str, text_only : bool = True) -> Context:
        """Generates a context from a pdf"""
        if not os.path.isfile(pdf_fpath):
            raise FileNotFoundError(f'File {pdf_fpath} not found')

        with tempfile.TemporaryDirectory() as tmp_dir:
            print(f'-> Converting pdf {pdf_fpath} to markdown in {tmp_dir}')
            PdfParser.to_markdown(fpath=pdf_fpath, target_dirpath=tmp_dir)
            print(f'-> Loading markdown into context')
            context = Context.from_markdown(source_dirpath=tmp_dir, text_only=text_only)
        return context

    @classmethod
    def from_markdown(cls, source_dirpath : str, text_only : bool = True) -> Context:
        """Generates a context from a directory with a markdown.md file and accompanying images"""

        # print(f'Reading markdown from source dirpath {source_dirpath}')
        markdown_fpath = os.path.join(source_dirpath, 'markdown.md')
        with open(markdown_fpath, 'r') as f:
            md_text = f.read()
        lines = md_text.split('\n')
        lines = [f'{j}_{line}' for j, line in enumerate(lines)]
        md_text = '\n'.join(lines)
        segments = Context._split_markdown(md_text)

        context = Context()
        for i, seg in enumerate(segments):
            is_image = i % 2

            if is_image and not text_only:
                msg = Message.from_img(msg='', img_fpath=os.path.join(source_dirpath, seg))
            elif is_image and text_only:
                continue
            else:
                msg = Message(text_content=seg)
            context.append(msg)

        return context

    @classmethod
    def from_latex(cls, source_dirpath: str, text_only: bool = True) -> Context:
        """Generates a context from a latex.tex file"""

        if not text_only:
            raise NotImplementedError('Latex images not yet supported')
        latex_fpath = os.path.join(source_dirpath, 'latex.tex')
        with (open(latex_fpath, 'r')) as f:
            latex_text = f.read()
            return Context.singleton(content=latex_text)


    @staticmethod
    def _split_markdown(md_text : str) -> list[str]:
        pattern = r'!\[[^\]]*\]\(([^)]+)\)'
        segments = []
        last_pos = 0

        for match in re.finditer(pattern, md_text):
            segments.append(md_text[last_pos:match.start()])
            segments.append(match.group(1))
            last_pos = match.end()

        if last_pos < len(md_text):
            segments.append(md_text[last_pos:])

        return segments

    def __add__(self, other) -> Context:
        return Context(super().__add__(other))

    def __str__(self):
        total_str = ''
        for msg in self:
            total_str += f'{msg.role}: {msg.text_content}'
        return total_str

if __name__ == "__main__":
    pdf_context = Context.from_pdf(pdf_fpath='../eval/smol_example.pdf')