# LinguoPDF — project setup helpers

Quick helper files added to this repository to make development easier.

Files added:
- `.gitignore` — comprehensive ignore for Python, Windows, VS Code, virtualenvs, Streamlit, and other artifacts.
- `.env.example` — example environment variables. Copy to `.env` and fill secrets.
- `requirements.txt` — recommended dependencies for Streamlit + PDF + LLM workflows.
- `scripts/env_manage.py` — small helper to `init`, `validate`, and `show` `.env` values.

Setup (Windows PowerShell):

```powershell
# create venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1
# install deps
pip install -r requirements.txt
# create .env from example
python .\scripts\env_manage.py init
# validate required keys (e.g. OPENAI_API_KEY)
python .\scripts\env_manage.py validate
# run Streamlit app
streamlit run .\app.py
```

Notes:
- Do NOT commit a real `.env` file — only commit `.env.example`.
- Adjust `requirements.txt` as needed for your exact LLM / PDF tooling choices.
