import streamlit as st
import pandas as pd 
import numpy as np
import openai

# for it to pop up on the sidebar
st.sidebar.markdown("# Home 🏠")

# title
st.title('SafeStay San Jóse (SS-SJ)')

# introduction
st.write = "Hi! Welcome to Our-program-name!" \
"We are here to aid you in your EIH needs."
st.write += "Please come and explore our applications for your needs!"

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
