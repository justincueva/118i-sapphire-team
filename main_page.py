import streamlit as st
import pandas as pd 
import numpy as np
import openai
from openai import OpenAI
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# title
st.title('SmartHaven')

# introduction
st.text ("Hi! Welcome to SmartHaven! We are here to aid you in your EIH needs.")
st.text("Please come and explore our applications for your needs!")

# for table of contents
st.subheader('Table of Contents', divider= 'blue')
message = "Come explore our many resources! We aim to help streamline ur EIH process." 
col1, col2 = st.columns(2)
with col1:
   st.page_link("pages/AI_Housing_Chat_Assistant.py", label="AI Housing Chat Assistant", icon="💬")
   st.page_link("pages/AI_Intake_Assistant.py", label="AI Intake Assistant", icon="🧠")
   st.page_link("pages/AI_Resource_Recommender.py", label="AI Resource Recommender", icon="🎯")
   st.page_link("pages/EIH_Budget_Overview.py", label="EIH Budget Overview", icon="💰")
   st.page_link("pages/Eligibility_&_Requirements.py", label="Eligibility & Requirements", icon="📋")


with col2:
   st.page_link("pages/Language_&_Communication_Tools.py", label="Language & Communication Tools", icon="💬")
   st.page_link("pages/Prototype.py", label="Prototype", icon="🔒")
   st.page_link("pages/Reddit_Sentiment_Analyzer.py", label="Reddit Sentiment Analyzer", icon="🔒")
   st.page_link("pages/Resources_&_Help.py", label="Resources & Help", icon="🆘")
   st.page_link("pages/Stakeholder_Involvement.py", label="Stakeholder Involvement", icon="🤝")


# button to apply for emergency housing or directed to it
# Clear call-to-action: “Apply for Emergency Housing”

# general crisis hotline or emergency contacts displayed prominently
# for contact info for the shelter hotline
st.subheader('Emergency Contacts', divider= 'blue')
st.write = "If you are seeking emergency hotlines, here are some contacts!"
st.markdown('''
For further assistance or inquiries: 
            
- **Here4You Shelter Hotline**: **(408) 385-2400** (Available daily from 9:00 AM to 7:00 PM)
- **Email**: [homewardbound@sanjoseca.gov](mailto:homewardbound@sanjoseca.gov)
- **Address**: 200 E. Santa Clara St., San José, CA 95113
- **TTY**: **(800) 735-2922**
''')

st.write = " If you want to see more tailored resources, check out our resources page!"
st.page_link("pages/Resources_&_Help.py", label="Resources & Help", icon="🆘")

# footer
st.markdown("---")
st.caption("Provided by the Sapphire Team 💎 • Powered by OpenAI & Streamlit ")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# for it to pop up on the sidebar
st.sidebar.markdown("# Home 🏠")
st.sidebar.markdown("---")

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

# Display full chat history in the sidebar
#   for sender, message in st.session_state.chat_history:
#      if sender == "You":
#         st.sidebar.markdown(f"🧍 **{sender}:** {message}")
#      else:
#         st.sidebar.markdown(f"🤖 **{sender}:** {message}")
