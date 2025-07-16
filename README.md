# Sentinel

**Sentinel** is a local AI assistant powered by Ollama's Phi-3 model. It accepts natural language commands and performs structured tasks — such as generating formal leave letters and exporting them to PDF — using Microsoft Word via COM automation.

## Features

- Local LLM processing using Ollama (Phi-3)
- Parses structured intent from natural language
- Generates formatted letter content
- Creates `.docx` using `python-docx`
- Converts to `.pdf` using `docx2pdf`
- Saves output directly to user's desktop

## Usage

```bash
python run.py
````

Then, input a command like:

```
Write a formal leave letter for 2 days and save it as PDF on desktop.
```

## Notes

* Word automation is Windows-specific.
* Timeout errors may occur if the local model is cold or under heavy load. Run `ollama run phi3` once manually before using the assistant.
