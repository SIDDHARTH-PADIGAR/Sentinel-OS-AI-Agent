from .ms_word_writer import WordWriter

def write_document(task_data):
    title = task_data.get("title", "Generated Document")
    content = task_data.get("content", "")
    writer = WordWriter(title=title, content=content, export_pdf=True)
    return writer.run()
