# OpenAI Python App

A small Python project that sends a hard-coded programming-joke prompt to the
Google Gemini API and prints the response. The project uses Google's
`google-genai` SDK.

## Requirements

- Python 3.10 or later
- A Gemini API key

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your Gemini API key:

```dotenv
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash
```

Keep the real API key private. The `.env` file is excluded from Git.

## Run

```bash
python main.py
```

The script loads `.env`, calls the configured Gemini model with a programming
joke prompt, and prints the generated text. `GEMINI_MODEL` is optional; if it
is not set, the script defaults to `gemini-3.8-flash`.

## Troubleshooting

- If the script reports a missing API key, make sure `.env` exists in the
  project root and defines `GEMINI_API_KEY`.
- A Google API `503` service-unavailable response indicates a temporary
  service issue. Retry later or configure another model available to your
  account using `GEMINI_MODEL`.
