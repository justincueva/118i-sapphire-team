import streamlit as st
import pandas as pd 
import numpy as np
import openai
import os
from openai import OpenAI

# for it to pop up on the sidebar
st.sidebar.markdown("# AI Intake Assistant 🧠")


# Set up the Streamlit page
st.title("🧠 AI Intake Assistant")
st.caption("Describe your housing situation. Let AI suggest next steps based on your story.")

st.markdown("---")
st.header("💬 Describe Your Current Situation")

# Get user input
user_input = st.text_area(
    label="Enter details about your housing situation below:",
    placeholder="e.g., I lost my job and can't pay rent. I have a dog and need shelter urgently.",
    height=200
)

# Initialize OpenAI client (hardcoded for now, replace with os.getenv for production)
client = OpenAI(api_key="OPENAI_API_KEY")

# Analyze button
if st.button("🧠 Analyze Situation and Suggest Help"):
    if not user_input.strip():
        st.warning("Please write something about your situation.")
    else:
        with st.spinner("AI is reading your story..."):
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You're a social worker AI helping people find emergency housing."},
                    {"role": "user", "content": f"My situation: {user_input}\nWhat emergency housing steps should I take?"}
                ]
            )
            result = response.choices[0].message.content
            st.success("✅ Suggested Steps:")
            st.markdown(result)

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