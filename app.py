import streamlit as st
from mentor.llm_interface import explain_code
from mentor.utils import static_warnings

st.set_page_config(page_title="Code Mentor Bot", layout="centered")

st.title("🤖 Code Mentor Bot")
st.markdown("Enter a code snippet below and get an explanation, powered by a local LLM.")

# 🔹 Sidebar model selector
model_choice = st.sidebar.selectbox(
    "Select a model",
    options=["phi", "codellama", "mistral"],
    index=0,
    help="Choose an Ollama model to use"
)

code_input = st.text_area("✍️ Paste your code here", height=200, placeholder="e.g. def factorial(n): ...")

if st.button("🔍 Explain"):
    if code_input.strip():
        warnings = static_warnings(code_input)
        if warnings:
            st.markdown("### ⚠️ Warnings before explaining:")
            for w in warnings:
                st.warning(w)

        with st.spinner(f"Explaining using {model_choice}..."):
            explanation = explain_code(code_input, model=model_choice)
            st.markdown("### 💡 Explanation:")
            st.write(explanation)
    else:
        st.warning("Please enter some code to explain.")
