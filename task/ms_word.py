from docx import Document
import os
import time
import re
import traceback
import win32com.client

def sanitize_filename(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[\\/*?\"<>|]", "_", text)
    return text.replace(" ", "_")

def write_document(payload: dict) -> str:
    print(f"--- Incoming Payload ---\n{payload}\n")

    title = payload.get("title") or "untitled"
    content = payload.get("content")
    file_format = (payload.get("format") or "word").strip().lower()

    if not isinstance(content, str) or not content.strip():
        raise ValueError("No valid content provided.")

    sanitized_title = sanitize_filename(title)
    timestamp = int(time.time())
    base_filename = f"{sanitized_title}_{file_format}_{timestamp}"

    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    os.makedirs(desktop, exist_ok=True)

    docx_path = os.path.join(desktop, f"{base_filename}.docx")
    pdf_path = os.path.join(desktop, f"{base_filename}.pdf")
    file_path = docx_path

    # Write to .docx
    try:
        doc = Document()
        for line in content.strip().split("\n"):
            doc.add_paragraph(line)
        doc.save(docx_path)
        print(f"Saved DOCX: {docx_path}")
    except Exception as e:
        print(f"Error saving .docx: {e}")
        raise

    # Convert to PDF
    if file_format == "pdf":
        try:
            print("Attempting PDF conversion via Word...")
            import win32com.client
            word = win32com.client.Dispatch("Word.Application")
            word.Visible = False
            pdf_doc = word.Documents.Open(docx_path)
            pdf_doc.SaveAs(pdf_path, FileFormat=17)
            pdf_doc.Close()
            word.Quit()
            file_path = pdf_path
            print(f"Saved PDF: {pdf_path}")
        except Exception as e:
            print("!!! PDF conversion failed. Falling back to .docx")
            traceback.print_exc()
            file_path = docx_path

    # Try to open the file
    try:
        os.startfile(file_path)
    except Exception as e:
        print(f"Could not open file automatically: {e}")

    print("\nPress ENTER after reviewing the document...", end='', flush=True)
    input()
    return file_path
