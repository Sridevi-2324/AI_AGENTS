# app.py

import streamlit as st
from router import build_graph

st.set_page_config(page_title="LLM Router", layout="centered")
st.title("🔁 LLM Input Router with LangGraph")

user_input = st.text_area("Enter your question, code request, or math problem:", height=150)

if st.button("Submit"):
    if user_input.strip():
        graph = build_graph()
        result = graph.invoke({"input": user_input})
        st.markdown(f"**Routed Category:** {result['category']}")
        st.markdown("**Response:**")
        st.code(result["output"], language="markdown")
    else:
        st.warning("Please enter something first.")
