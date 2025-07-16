import os
from docx import Document
from llm.local_llm import get_letter_content
from utils.win_tools import get_desktop_path

def create_letter(task):
    print("Writing letter...")

    # Prompt the LLM to generate the content of the letter
    content_prompt = f"Write a {task['tone']} leave letter for {task['duration']}."
    try:
        content = get_letter_content(content_prompt)
    except Exception as e:
        print("Failed to get content from Phi-3:")
        print(e)
        return

    # Create the Word document
    doc = Document()
    doc.add_paragraph(content)

    # Determine where to save the .docx
    desktop = get_desktop_path() if task["destination"] == "desktop" else task["destination"]
    destination_path = os.path.join(desktop, "leave_letter.docx")

    # Ensure folder exists
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    try:
        doc.save(destination_path)
        print(f".docx saved at: {destination_path}")
    except Exception as e:
        print("Failed to save .docx:")
        print(e)
        return

    # If the user wants a PDF, convert it
    if task["output_format"].lower() == "pdf":
        try:
            from docx2pdf import convert
            convert(destination_path)
            print("Converted to PDF.")
        except Exception as e:
            print("PDF conversion failed:")
            print(e)
