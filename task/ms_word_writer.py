from docx import Document
import os
import time
import re
import traceback

class WordWriter:
    def __init__(self, title: str, content: str, export_pdf: bool = False):
        self.title = title.strip() or "Generated_Document"
        self.content = content
        self.export_pdf = export_pdf
        self.timestamp = int(time.time())
        self.base_filename = self._sanitize_filename(f"{self.title}_{self.timestamp}")
        self.desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        os.makedirs(self.desktop, exist_ok=True)
        self.docx_path = os.path.join(self.desktop, f"{self.base_filename}.docx")
        self.pdf_path = os.path.join(self.desktop, f"{self.base_filename}.pdf")

    def _sanitize_filename(self, text: str) -> str:
        return re.sub(r'[\\/*?:"<>|]', '_', text).replace(" ", "_")

    def _write_docx(self):
        doc = Document()
        for line in self.content.strip().split("\n"):
            doc.add_paragraph(line)
        doc.save(self.docx_path)

    def _convert_to_pdf(self):
        try:
            import win32com.client
            word = win32com.client.Dispatch("Word.Application")
            word.Visible = False
            doc = word.Documents.Open(self.docx_path)
            doc.SaveAs(self.pdf_path, FileFormat=17)
            doc.Close()
            word.Quit()
            return self.pdf_path
        except Exception as e:
            traceback.print_exc()
            return self.docx_path

    def run(self):
        self._write_docx()
        final_path = self._convert_to_pdf() if self.export_pdf else self.docx_path
        try:
            os.startfile(final_path)
        except Exception as e:
            print(f"Could not open file: {e}")
        return final_path
