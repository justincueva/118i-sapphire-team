import streamlit as st
import pandas as pd
import openai
import os

# for it to pop up on the sidebar
st.sidebar.markdown("# EIH Budget Overview 💰")

# Page setup
st.title("💰 EIH Budget Overview")

# Budget data
data = {
    'Category': [
        'Facility Leasing', 'Staff Wages', 'Food & Supplies',
        'Mental Health', 'Security', 'Transportation', 'Admin'
        ],
    'Cost': [1200000, 850000, 500000, 400000, 200000, 150000, 100000]
    }
df = pd.DataFrame(data)

# Show table and bar chart
st.header("📊 Budget Breakdown")
st.dataframe(df)
st.bar_chart(df.set_index("Category"))

# Total cost
total = df["Cost"].sum()
st.metric("Total Budget", f"${total:,}")

# Funding
st.header("💬 Funding Sources")
funding_total = 1000000 + 800000 + 600000 + 300000
st.write=("- HUD: $1,000,000")
st.write=("- State: $800,000")
st.write=("- City: $600,000")
st.write=("- Private: $300,000")

# Budget gap
st.header("🧮 Budget Gap")
gap = total - funding_total

if gap <= 0:
    st.success("Fully funded! 🎉")
else:
    st.error(f"Shortfall: ${gap:,}")
    st.write=("Suggestions:")
    st.write=("- Apply for FEMA")
    st.write=("- Start donor campaign")


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