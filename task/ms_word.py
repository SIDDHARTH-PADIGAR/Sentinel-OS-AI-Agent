import os
import tempfile
import subprocess
from docx import Document
from llm.local_llm import get_letter_content
from utils.win_tools import get_desktop_path

def create_letter(task):
    print("Writing letter...")

    content_prompt = f"Write a {task['tone']} leave letter for {task['duration']}."
    try:
        content = get_letter_content(content_prompt)
    except Exception as e:
        print("Failed to get content from Mistral:")
        print(e)
        return

    # Step 1: Save draft to temp file
    draft_path = os.path.join(tempfile.gettempdir(), "leave_letter_draft.docx")
    doc = Document()
    doc.add_paragraph(content)
    doc.save(draft_path)
    print(f"Draft saved to temp: {draft_path}")

    # Step 2: Open Word for review
    try:
        os.startfile(draft_path)  # opens in MS Word
    except Exception as e:
        print("Failed to open draft in Word:")
        print(e)
        return

    # Step 3: Wait for user confirmation
    input("\nReview the letter. Press Enter to finalize and save...")

    # Step 4: Save final .docx
    desktop = get_desktop_path() if task["destination"] == "desktop" else task["destination"]
    destination_path = os.path.join(desktop, "leave_letter.docx")
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    try:
        doc.save(destination_path)
        print(f"Final .docx saved at: {destination_path}")
    except Exception as e:
        print("Failed to save final .docx:")
        print(e)
        return

    # Step 5: Convert to PDF if requested
    if task["output_format"].lower() == "pdf":
        try:
            from docx2pdf import convert
            convert(destination_path)
            print("Converted to PDF.")
        except Exception as e:
            print("PDF conversion failed:")
            print(e)
