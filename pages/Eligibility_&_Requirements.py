import streamlit as st
import pandas as pd 
import numpy as np
import openai

# for it to pop up on the sidebar
st.sidebar.markdown("# Eligibility & Requirements 📋")

# page title
st.title('Eligibility & Requirements 📋')
st.write = ('Learn about who qualifies for emergency interim housing, what documents you will need, and how to prepare for the application process.')


# introduction
st.write = ('Welcome to the Emergency Interim Housing (EIH) program information page. Here, you ' \
'will find details on eligibility criteria, the application process, and resources ' \
'available for individuals and families experiencing homelessness in San José and Santa Clara County.')

# for the qualifications
st.subheader('Qualifications for EIH', divider= 'blue')
st.markdown('''
To qualify for the EIH program, applicants must meet the following requirements:

- **Residency**: Must be a resident of Santa Clara County.
- **Homeless Status**: Must be currently experiencing homelessness.
- **Assessment**: Completion of the Vulnerability Index-Service Prioritization Decision Assistance Tool (VI-SPDAT) to determine housing and service needs. 
[Learn more about Coordinated Entry and VI-SPDAT](https://osh.sccgov.org/continuum-care/coordinated-entry)
- **Special Populations**: Certain programs may prioritize specific groups, such as:
  - Transition-aged youth (16 to 24 years old)
  - Domestic violence survivors
  - Individuals in recovery from substance use disorders
  - Persons exiting the criminal justice system
  - [More information on targeted populations](https://osh.sccgov.org/solutions-homelessness/interim-solutions/transitional-housing)
''')

# for the req documents
st.subheader('Required Documents', divider= 'blue')
st.markdown('''
Here's a list of commonly required documents for EIH Applicants:
1. **Valid Government-Issued Photo ID**
    - e.g., Driver’s License, State ID, Passport
2.  **Proof of Homelessness**
    - Letter from a shelter, outreach worker, or case manager
    - Self-certification form if no other proof is available
3. **Proof of Income** (if any)
    - Pay stubs, unemployment benefits, SSI/SSDI documentation
    - Bank statements (optional, depending on program)
4. **Referral from a Case Manager or Outreach Team**
    - Required for most San Jose EIH placements (e.g., from Destination:Home, HomeFirst, or City outreach teams)
5. **Social Security Card or Number**
    - For background checks and service eligibility
6. **Medical or Disability Documentation** (if applicable)
    - To prioritize individuals with medical needs or vulnerabilities
7. **Proof of Santa Clara County Residency** (sometimes optional)
    - Mail, benefits documentation, or ID with a local address
''')

# for the app process
st.subheader('Application Process', divider= 'blue')
st.markdown(
'''1. **Initial Contact**:
   - **Here4You Hotline**: Call **(408) 385-2400** between 9:00 AM and 7:00 PM, seven days a week, to connect with a representative who can assist with shelter placements. 
   [More details](https://osh.sccgov.org/solutions-homelessness/interim-solutions/emergency-shelters)
   - **Coordinated Entry Assessment**: Schedule an appointment to complete the VI-SPDAT assessment.
2. **Documentation**: Prepare necessary documents, which may include:
   - Identification (e.g., driver's license, state ID)
   - Proof of Santa Clara County residency
   - Any relevant medical or legal documents
3. **Program Referral**: Based on assessment results, you may be referred to an appropriate housing program that fits your needs.

*Note*: Availability is limited, and placement is not guaranteed. It's essential to maintain communication with your case manager and explore multiple housing options.
''')

# for the faq
st.subheader('FAQs for common situations', divider= 'blue')
st.markdown('''
1. **Who is eligible for Emergency Interim Housing?**  
    EIH is primarily for individuals and families experiencing homelessness 
    who are referred by outreach teams or service providers in Santa Clara County.
2.  **Do I need a referral to apply?**  
    Yes, most EIH placements require a referral from a case manager, outreach team, 
    or local nonprofit partner.
3. **Is there a cost to stay in EIH?**  
    No, EIH programs are typically funded by the City and County and are free for eligible residents.
4. **How long can I stay in an EIH unit?**  
    Length of stay varies, but it is designed to be temporary housing while residents 
    transition into more permanent solutions.
5. **Can I bring my pet?**  
    Some EIH sites are pet-friendly. Please confirm with the site or your case manager.
6. **What services are offered at EIH sites?**  
    Residents typically have access to case management, meals, hygiene services, mental 
    health support, and housing navigation.
7. **Do I need to show proof of income?**  
    Proof of income is not always required, but it may help case managers tailor support 
    services or future housing plans.
8. **Can I apply directly on this site?**  
    No, direct applications are not accepted. You will need to connect with an outreach worker 
    or case manager to start the process.
9. **Is language assistance available?**  
    Yes! Translation tools and speech bots are available on this site, and staff are trained to 
    assist non-English speakers.
10. **What if I don’t have all the documents?**  
    Don’t worry—case managers can help you gather necessary documents or help you self-certify if needed.
''')

# for the references they can press/websites
st.subheader('Additional References', divider= 'blue')
st.markdown(
'''- **Homeless Resource Guide**: A comprehensive guide to services available for individuals experiencing homelessness in San José.
  - [English Guide](https://www.sanjoseca.gov/your-government/departments-offices/housing/homelessness-response/homeless-families-individuals)
  - [Guía en español](https://www.sanjoseca.gov/your-government/departments-offices/housing/homelessness-response/homeless-families-individuals)
  - [Tài liệu hướng dẫn bằng tiếng Việt](https://www.sanjoseca.gov/your-government/departments-offices/housing/homelessness-response/homeless-families-individuals)
- **Office of Supportive Housing**: Provides information on various housing programs and services in Santa Clara County. [Visit their website](https://osh.sccgov.org/)
- **Emergency Shelters**: For immediate shelter needs, contact the Here4You Hotline at **(408) 385-2400**. [More information](https://osh.sccgov.org/solutions-homelessness/interim-solutions/emergency-shelters)
''')

# footer
st.markdown("---")
st.caption("Provided by the Sapphire Team 💎 • Powered by OpenAI & Streamlit")
st.caption("lines this-this was generated by ChatGPT")