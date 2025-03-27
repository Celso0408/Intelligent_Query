from __future__ import annotations

from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

from marker.logger import configure_logging
import traceback

import os
import mistletoe
from mistletoe.latex_renderer import LaTeXRenderer

os.environ["IN_STREAMLIT"] = "true"
os.environ["PDFTEXT_CPU_WORKERS"] = "1"

configure_logging()

# ---------------------------------------


class PdfParser:
    @staticmethod
    def to_markdown(fpath : str, target_dirpath : str, format_tables : bool = True):
        """Converts pdf to directory with markdown.md file + images"""
        try:
            converter = PdfConverter(artifact_dict=create_model_dict())
            rendered = converter(filepath=fpath)
            full_text, _, images = text_from_rendered(rendered)

            if format_tables:
                full_text = PdfParser._attempt_table_formatting(text=full_text)

            PdfParser._save_markdown(target_dirpath=target_dirpath, full_text=full_text, images=images)

        except Exception as e:
            print(f"Error converting {fpath}: {e}")
            print(traceback.format_exc())
            raise e

    @staticmethod
    def to_latex(md_dirpath : str, target_dirpath : str):
        """Converts markdown file markdown.md to Latex"""
        fpath = f'{md_dirpath}/markdown.md'
        with open(fpath, 'r') as fin:
            rendered = mistletoe.markdown(fin, LaTeXRenderer)
        os.makedirs(target_dirpath, exist_ok=True)
        with open(f'{target_dirpath}/latex.tex', 'w') as fout:
            fout.write(rendered)


    @staticmethod
    def _attempt_table_formatting(text : str) -> str:
        tables = PdfParser.get_tables(text)
        for t in tables:
            try:
                new_table = PdfParser.format_table(t)
                text = text.replace(t, new_table)
            except:
                pass
        return text

    @staticmethod
    def _save_markdown(target_dirpath : str, full_text : str, images):
        os.makedirs(target_dirpath, exist_ok=True)

        fpath = os.path.join(target_dirpath, 'markdown.md')
        with open(fpath, "w+", encoding='utf-8') as f:
            f.write(full_text)

        for filename, image in images.items():
            image_filepath = os.path.join(target_dirpath, filename)
            image.save(image_filepath, "PNG")


    @staticmethod
    def get_tables(content : str) -> list[str]:
        tables = []
        lines = content.split('\n')
        in_table = False
        current_table = ''
        for j, l in enumerate(lines):
            line_is_table = l.startswith('|') and l.endswith('|')
            if line_is_table:
                in_table = True
            if in_table:
                current_table += f'{l}\n'
            if in_table and not line_is_table:
                print(f'Detected table: {current_table}')
                tables.append(current_table)
                in_table = False
                current_table = ''

        return tables


    @staticmethod
    def format_table(table_content : str) -> str:
        lines = table_content.split('\n')
        num_cols = len(lines[0].split('|'))
        print(f'Formatting table = {table_content}')

        table = []
        max_col_lens = [0] * num_cols

        for row in lines:
            entries = row.split('|')
            table.append(entries)
            for j, item in enumerate(entries):
                max_col_lens[j] = max(max_col_lens[j], len(item))

        max_col_lens = max_col_lens[1:-1]
        print(f'Col lens = {max_col_lens}')

        formatted_table = ''
        for row in table:
            row_str = ''
            row = row[1:-1]
            for j, entry in enumerate(row):
                max_len = max_col_lens[j]
                row_str += f'|{entry:<{max_len}}|'
            formatted_table += f'{row_str}\n'

        return formatted_table


if __name__ == "__main__":
    pass
    # test_md_dirpath = '/home/daniel/sciai/pdfquery/data/curated/markdown'
    # for name in os.listdir(test_md_dirpath):
    #     markdown_fpath = os.path.join(test_md_dirpath, name, 'markdown.md')
    #     with open(markdown_fpath, 'r') as f:
    #         content = f.read()
    #
    # # md_fpath = '/home/daniel/sciai/pdfquery/data/curated/markdown/foreign1/markdown.md'
    # with open(md_fpath, 'r') as f:
    #     content = f.read()
    #     tables = Parser.get_tables(content)
    #     print(f'No tables = {len(tables)}')
    #
    #     print(Parser._attempt_table_formatting(content))