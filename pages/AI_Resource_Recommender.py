import streamlit as st
import pandas as pd 
import numpy as np
import openai
import os
from openai import OpenAI

# for it to pop up on the sidebar
st.sidebar.markdown("# AI Resource Recommender 🎯")


st.title("🎯 AI Resource Recommender")
st.caption("Select your needs and let AI recommend relevant services in your city.")

openai.api_key = os.getenv("OPENAI_API_KEY")

st.markdown("---")
st.header("📦 Choose Your Needs")

needs = st.multiselect(
    "Select the services you need help with:",
    ["Meals", "Mental Health Support", "Job Assistance", "Medical Access", "Family Shelter", "Pet-Friendly Housing"]
)

user_city = st.text_input("What city are you in?", placeholder="e.g., San Jose")

if st.button("🔍 Get AI-Powered Resource Suggestions"):
    if not needs:
        st.warning("Please select at least one need.")
    elif not user_city:
        st.warning("Please enter your city.")
    else:
        prompt = f"I'm in {user_city}. I need services for: {', '.join(needs)}. Recommend resources and a short explanation for each."
        with st.spinner("Finding personalized resources..."):
            chat = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You're an AI that recommends real local services for housing and social support."},
                    {"role": "user", "content": prompt}
                ]
            )
            st.success("📋 AI Suggestions:")
            st.markdown(chat.choices[0].message.content)


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