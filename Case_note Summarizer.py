
✅ Page 2: eih_2_ai_service_recommender.py
python
Copy
Edit
import streamlit as st
import openai
import os

st.set_page_config(page_title="AI Resource Recommender", layout="wide")
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
✅ Page 3: eih_3_case_note_summarizer.py
python
Copy
Edit
import streamlit as st
import openai
import os

st.set_page_config(page_title="AI Case Note Summarizer", layout="wide")
st.title("✍️ AI Case Note Summarizer")
st.caption("Paste long staff notes below and get a quick, human-readable summary.")

openai.api_key = os.getenv("OPENAI_API_KEY")

st.markdown("---")
st.header("📄 Paste Long Case Notes")

notes = st.text_area("Enter the full notes here:", height=300, placeholder="Client is currently living in their vehicle...")

if st.button("✂️ Summarize Notes"):
    if not notes.strip():
        st.warning("Please enter some notes.")
    else:
        with st.spinner("Summarizing..."):
            chat = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an assistant that summarizes case manager notes into 3 bullets."},
                    {"role": "user", "content": f"Summarize these notes:\n\n{notes}"}
                ]
            )
            st.success("📝 Summary:")
            st.markdown(chat.choices[0].message.content)
