# 💡 Lumos

> AI-powered CLI that explains compiler and runtime errors in plain English.

Lumos is a command-line tool that analyzes compiler and terminal errors using Large Language Models (LLMs). Prefix your command with `lumos run` and receive a structured explanation, root cause analysis, and actionable debugging steps directly in your terminal.

---

## ✨ Features

- 🤖 AI-powered error explanation
- 💻 Works directly from the terminal
- 🌐 Language-agnostic architecture
- 🛠 Root cause analysis
- 📖 Step-by-step debugging suggestions
- 🎨 Beautiful terminal output using Rich
- ⚡ Falls back to the original error if AI analysis fails

---

## 🚀 Demo

Instead of running

```bash
python app.py
```

Run

```bash
lumos run python app.py
```

Instead of seeing:

```text
Traceback (most recent call last):
  File "app.py", line 1
    print(hello world)
          ^^^^^^^^^^^
SyntaxError: invalid syntax
```

Lumos displays:

```
❌ Error Summary
────────────────────────────
The error occurred because the text
"hello world" is not enclosed in quotes.

🔍 Root Cause
────────────────────────────
Python interpreted hello and world as
identifiers instead of a string.

🛠 Debugging Steps
────────────────────────────
• Wrap the text inside quotes.
• Change

    print(hello world)

  to

    print("hello world")

📊 Confidence
100%
```

---

# 🏗 Architecture

```
                User Command
                     │
                     ▼
         lumos run python app.py
                     │
                     ▼
             Process Runner
                     │
        stdout / stderr / exit code
                     │
                     ▼
             Log Normalizer
                     │
                     ▼
             Parsed Error Object
                     │
                     ▼
               FastAPI Backend
                     │
                     ▼
              Prompt Generator
                     │
                     ▼
               LLM Inference API
                     │
                     ▼
          Structured JSON Response
                     │
                     ▼
            Rich Terminal Formatter
                     │
                     ▼
                User-friendly Output
```

---


# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/lumos.git
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

Install the CLI

```bash
cd cli
pip install -e .
```

Start the backend

```bash
cd ../backend
python main.py
```

---

# 🚀 Usage

General syntax

```bash
lumos run <command>
```

Examples

```bash
lumos run python app.py

lumos run node app.js

lumos run java Main

lumos run go run main.go

lumos run demo.exe
```

---

# 🌍 Supported Languages

Lumos is language-agnostic and currently works with commands from languages such as:

- Python
- JavaScript / Node.js
- Java
- C++
- C
- C#
- Go
- Rust
- Any executable that returns an error through the terminal

---

# 🛠 Tech Stack

### CLI

- Python
- Typer
- Rich
- Requests

### Backend

- FastAPI
- Uvicorn

### AI

- Hugging Face Inference API
---

# 🎯 Current Capabilities

- ✅ Compiler errors
- ✅ Syntax errors
- ✅ Exception analysis
- ✅ Human-readable explanations
- ✅ Root cause identification
- ✅ Debugging suggestions
- ✅ Confidence score
- ✅ Original error fallback when AI is unavailable

---

