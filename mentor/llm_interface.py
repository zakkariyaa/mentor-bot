import ollama

def explain_code(code: str, model: str = "phi") -> str:
    prompt = f"Explain what the following code does:\n```python\n{code}\n```"
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    return response['message']['content']
