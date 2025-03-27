import os
import tempfile

from holytools.devtools import Unittest

from data.providers import FileProvider
from pdfquery.pdfparser import PdfParser

# ---------------------------------------------

class TestPdfConversion(Unittest):
    def setUp(self):
        self.resources : FileProvider = FileProvider()

    def test_to_markdown(self):
        pdf_fpath = self.resources.get_graphite_paper_fpath()
        temp_dir = tempfile.mktemp()
        PdfParser.to_markdown(fpath=pdf_fpath, target_dirpath=temp_dir)

        markdown_fpath = os.path.join(temp_dir, 'markdown.md')
        self.assertTrue(os.path.isfile(markdown_fpath))

        with open(markdown_fpath, 'r') as f:
            md_text = f.read()
            self.assertIn('Comparative study', md_text)


if __name__ == "__main__":
    TestPdfConversion.execute_all()