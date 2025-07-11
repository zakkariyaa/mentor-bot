# 🤖 Code Mentor Bot

**Code Mentor Bot** is a local-first AI assistant that explains code snippets (fully offline), with no API calls or cloud dependencies.

Powered by:
- 🧠 Local LLMs via [Ollama](https://ollama.com/)
- 🖥️ Lightweight [Streamlit](https://streamlit.io/) UI
- 🧰 Supports models like `phi`, `codellama`, and `mistral`

![demo-gif](https://github.com/zakkariyaa/mentor-bot/blob/main/mentor-bot.png)  
<sub>Live explanation of a function that adds two numbers using a local model</sub>

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
git clone https://github.com/zakkariyaa/mentor-bot.git
cd mentor-bot
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Clone and set up environment
Install Ollama: https://ollama.com/download
Then run:

```bash
ollama pull phi
ollama pull codellama
ollama pull mistral
```

### 3. Run the app
```bash
streamlit run app.py
```
💡 Example Input
```python
def factorial(n):
    return n * factorial(n - 1)
```

🧪 Run Tests
```bash
pytest -m "not slow"        # Fast tests only
pytest                      # All tests, including slow LLM tests
```
![Tests](https://github.com/zakkariyaa/mentor-bot/actions/workflows/ci.yml/badge.svg)

✨ Why This Project?
Built to demonstrate:

🔒 Offline-friendly AI toolin <br />
🧠 LangChain-free LLM integration <br />
🧑‍💻 Thoughtful UX for code understanding <br />
