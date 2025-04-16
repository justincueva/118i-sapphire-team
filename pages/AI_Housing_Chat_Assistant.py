import streamlit as st
import pandas as pd 
import numpy as np
import openai
import os

# for it to pop up on the sidebar
st.sidebar.markdown("# AI Housing Chat Assistant 💬")

st.title("💬 AI Housing Chat Assistant")
st.caption("Chat with our AI for help understanding services, policies, or how to apply.")

openai.api_key = os.getenv("OPENAI_API_KEY")

st.markdown("---")
st.header("🤔 Ask any housing-related question")

query = st.chat_input("e.g., Can I apply for shelter if I have a pet?")

if query:
    with st.spinner("Thinking..."):
        answer = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert in emergency housing and social services."},
                {"role": "user", "content": query}
            ]
        )
        st.write("🤖 AI says:")
        st.markdown(answer.choices[0].message.content)

# footer
st.markdown("---")
st.caption("Provided by the Sapphire Team 💎 • Powered by OpenAI & Streamlit")