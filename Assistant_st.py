import streamlit as st
import openai
import os

st.set_page_config(page_title="AI Intake Assistant", layout="wide")
st.title("🧠 AI Intake Assistant")
st.caption("Describe your housing situation. Let AI suggest next steps based on your story.")

# SETUP
openai.api_key = os.getenv("OPENAI_API_KEY")

st.markdown("---")
st.header("💬 Describe Your Current Situation")

user_input = st.text_area(
    label="Enter details about your housing situation below:",
    placeholder="e.g., I lost my job and can't pay rent. I have a dog and need shelter urgently.",
    height=200
)

if st.button("🧠 Analyze Situation and Suggest Help"):
    if not user_input.strip():
        st.warning("Please write something about your situation.")
    else:
        with st.spinner("AI is reading your story..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You're a social worker AI helping people find emergency housing."},
                    {"role": "user", "content": f"My situation: {user_input}\nWhat emergency housing steps should I take?"}
                ]
            )
            result = response.choices[0].message.content
            st.success("✅ Suggested Steps:")
            st.markdown(result)
