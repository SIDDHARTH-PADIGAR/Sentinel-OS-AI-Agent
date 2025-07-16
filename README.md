# Sentinel

Sentinel is a Windows-native AI automation agent. It uses a local LLM (like Phi-3 via Ollama) to parse natural language tasks and automate desktop workflows like writing letters, managing files, and more.

## Example

What would you like me to do?
Write a formal leave letter for two days and save it as PDF on Desktop.

markdown
Copy
Edit

## Tech Stack
- Python
- Windows COM Automation (MS Word)
- Ollama + Phi-3
- Extensible plugin-based architecture

## Run it
```bash
python run.py
yaml
Copy
Edit

---

## NEXT STEPS:

1. Make sure you’ve installed:
   ```bash
   pip install pywin32
Verify ollama run phi3 is working standalone.

Run the CLI:

bash
Copy
Edit
python run.py
And tell it:

pgsql
Copy
Edit
Write a formal leave letter for 2 days and save it as PDF on desktop.