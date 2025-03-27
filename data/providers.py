import os
from enum import Enum

import mistletoe
import requests
from huggingface_hub import snapshot_download
from mistletoe.latex_renderer import LaTeXRenderer

from pdfquery.language import Context
from pdfquery.pdfparser import PdfParser

# -----------------------------------

class DocType(Enum):
    MARKDOWN : str = 'MARKDOWN'
    LATEX : str = 'LATEX'


class ContextProvider:
    def __init__(self):
        self.file_provider : FileProvider = FileProvider()

    def get_context(self, pid : str, doctype : DocType = DocType.MARKDOWN) -> Context:
        """Generates context from paper specified with paperID (pid)"""

        structured_dirpath = self.file_provider.get_structured_dirpath(pid=pid)
        if doctype.value == 'MARKDOWN':
            if not os.path.isfile(f'{structured_dirpath}/markdown.md'):
                self._generate_markdown(pid=pid)
            context = Context.from_markdown(source_dirpath=structured_dirpath)
        else:
            if not os.path.isfile(f'{structured_dirpath}/latex.tex'):
                self._generate_latex(pid=pid)
            context = Context.from_latex(source_dirpath=structured_dirpath)
        return context

    def _generate_markdown(self, pid : str):
        pdf_fpath = self.file_provider.get_pdf_fpath(pid=pid)
        if not os.path.isfile(pdf_fpath):
            raise FileNotFoundError(f"Failed to find PDF at {pdf_fpath}. Please download manually")

        md_dirpath = self.file_provider.get_structured_dirpath(pid=pid)
        PdfParser.to_markdown(fpath=pdf_fpath, target_dirpath=md_dirpath)

    def _generate_latex(self, pid : str):
        structured_dirpath = self.file_provider.get_structured_dirpath(pid=pid)
        md_fpath = f'{structured_dirpath}/markdown.md'
        if not os.path.isfile(md_fpath):
            self._generate_markdown(pid=pid)

        with open(md_fpath, 'r') as f:
            rendered = mistletoe.markdown(f, LaTeXRenderer)
            latex_fpath = os.path.join(structured_dirpath, 'latex.tex')
            with open(latex_fpath, 'w') as fout:
                fout.write(rendered)


class FileProvider:
    def __init__(self):
        self.data_dirpath : str = os.path.dirname(__file__)
        self.graphite_paper_name : str = 'phys1'
        self.curated_pdf_dirpath : str = os.path.join(self.data_dirpath, 'curated', 'pdf')
        self.spiqa_dirpath : str = os.path.join(self.data_dirpath, 'spiqa')
        if not os.path.isdir(self.spiqa_dirpath):
            snapshot_download(repo_id="google/spiqa", repo_type="dataset", local_dir=self.spiqa_dirpath)
        self.spiqa_jsonA_fpath : str = os.path.join(self.spiqa_dirpath, 'test-A/SPIQA_testA.json')
        self.spiqa_jsonB_fpath : str = os.path.join(self.spiqa_dirpath, 'test-B/SPIQA_testB.json')

    def get_pdf_fpath(self, pid : str):
        """Retrieves fpath of pdf with paperID pid"""
        return os.path.join(self.data_dirpath, 'curateed', 'pdf', f'{pid}.pdf')

    def get_structured_dirpath(self, pid : str):
        """Retrieves dirpath of structured representation of paper specified with paperID pid"""
        return os.path.join(self.data_dirpath, 'curated', 'structured', f'{pid}')

    def get_structured_fpath(self, pid : str, doc_type : DocType):
        """Retrieves fpath of structured representation file (markdown.md/latex.tex) of paper specified by paperID pid"""
        fname = f'markdown.md' if doc_type.value == 'MARKDOWN' else f'latex.tex'
        return os.path.join(self.get_structured_dirpath(pid=pid), fname)

    # ------------------------------------------

    @staticmethod
    def _download_arxiv_pdf(identifier : str, target_fpath : str):
        url = f"https://arxiv.org/pdf/{identifier}"
        response = requests.get(url)

        if response.status_code == 200:
            with open(target_fpath, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded arxiv/{identifier} from {url}")
        else:
            print(f"Failed to download PDF. Status code: {response.status_code}")


if __name__ == "__main__":
    # provider = FileProvider()
    # fpath = provider.get_pdf_fpath(mode=ResourceType.LOCAL, identifier='10.1088/0953-8984/27/41/415502')
    # print(fpath)

    context_provider = ContextProvider()
    context_provider._generate_latex(pid='phys1')