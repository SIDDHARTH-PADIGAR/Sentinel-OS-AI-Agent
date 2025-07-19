from task.ms_word_writer import WordWriter  # <- adjust path if needed

writer = WordWriter(
    title="Test Title",
    content="This is the first line.\nThis is the second line.",
    export_pdf=True
)
writer.run()
