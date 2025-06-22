# 🤖 Code Mentor Bot

**Code Mentor Bot** is a local-first AI assistant that explains code snippets — fully offline, with no API calls or cloud dependencies.

Powered by:
- 🧠 Local LLMs via [Ollama](https://ollama.com/)
- 🖥️ Lightweight [Streamlit](https://streamlit.io/) UI
- 🧰 Supports models like `phi`, `codellama`, and `mistral`

---

## 🧪 Demo

![demo-gif](demo.gif)  
<sub>Live explanation of recursive code using a local model</sub>

---

## 🚀 Features

- ✍️ Paste any Python (or general-purpose) code
- 🤖 Get instant explanations using offline models
- 🎛️ Switch between multiple models (phi, mistral, codellama)
- ⚠️ Smart static checks (e.g., recursion without base case)
- 🧪 Tested & CI-friendly with mocked LLM calls

---

## 🛠️ How to Run

> ⚠️ Python 3.10+ recommended

### 1. Clone and set up environment

```bash
git clone https://github.com/your-username/code-mentor-bot.git
cd code-mentor-bot
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
