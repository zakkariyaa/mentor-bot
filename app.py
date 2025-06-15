import streamlit as st
from mentor.llm_interface import explain_code

st.set_page_config(page_title="Code Mentor Bot", layout="centered")

st.title("🤖 Code Mentor Bot")
st.markdown("Enter a code snippet below and get an explanation, powered by a local LLM.")

code_input = st.text_area("✍️ Paste your code here", height=200, placeholder="e.g. def factorial(n): ...")

if st.button("🔍 Explain"):
    if code_input.strip():
        with st.spinner("Asking the model..."):
            explanation = explain_code(code_input)
            st.markdown("### 💡 Explanation:")
            st.write(explanation)
    else:
        st.warning("Please enter some code to explain.")
