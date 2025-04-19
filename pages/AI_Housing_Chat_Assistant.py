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

#------------------------------------------------------------------------------------------------------------------------------------------------------

# chatbot on the side
st.sidebar.title("💬 HelpBot")
st.sidebar.write("Need help with Emergency Interim Housing (EIH)? Ask anything.")

# Initialize chat history if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# user input area
user_input = st.sidebar.text_input("You:", key="user_input", placeholder="e.g., Can I apply for shelter if I have a pet?")

# If user submits a message
if user_input:
    # Add user message to chat history
    st.session_state.chat_history.append(("You", user_input))

    # Generate AI response using OpenAI
    with st.spinner("Thinking..."):
        try:
            messages = [{"role": "system", "content": "You are a helpful assistant that specializes in Emergency Interim Housing (EIH) in San Jose and Santa Clara County. Be concise, helpful, and clear."}]
            
            # Add all previous messages to maintain context
            for sender, message in st.session_state.chat_history:
                role = "user" if sender == "You" else "assistant"
                messages.append({"role": role, "content": message})

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
                temperature=0.6,
                max_tokens=500
            )

            bot_reply = response.choices[0].message.content.strip()
            st.session_state.chat_history.append(("Bot", bot_reply))

        except Exception as e:
            bot_reply = "⚠️ Sorry, I ran into an error. Please try again."
            st.session_state.chat_history.append(("Bot", bot_reply))
            st.error(f"Error: {e}")