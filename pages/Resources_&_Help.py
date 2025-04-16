import streamlit as st
import pandas as pd 
import numpy as np
import openai

# for it to pop up on the sidebar
st.sidebar.markdown("# Resources & Help 🆘 ")

# page title
st.title('Resources & Help 🆘 ')
st.text('For individuals seeking emergency interim housing and support services in San Jose, CA!')

# title for san jose resources
st.subheader('Resource Locations', divider='blue')
st.text('These resources are mainly listed for the San Jose/Santa Clara County area.')

   # for ___ housing
st.markdown('''
- **[HomeFirst Services](https://www.homefirstscc.org/)**  
  Services: Emergency shelters, transitional housing, outreach''')
   # for ___ housing
st.markdown('''
- **[Bill Wilson Center](https://www.billwilsoncenter.org/)**  
  Services: Youth & young adults, emergency shelter, family support''')
   # for ___ housing
st.markdown('''
- **[CityTeam San Jose](https://www.cityteam.org/san-jose)**  
  Services: Food, shelter, addiction recovery, and transitional housing''')

# ----------------------------------------------------------------
# for shelter locations
st.subheader('Emergency Shelters', divider= 'blue')

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.33, -121.88],
    columns=['lat', 'lon'])
st.map(df)
st.link_button("Click for more map examples", "https://docs.streamlit.io/develop/api-reference/charts/st.map")
   
# ----------------------------------------------------------------

# for local food banks and basic needs
st.subheader('Local Food Banks & Basic Needs', divider= 'blue')
st.markdown('''
- **[Second Harvest of Silicon Valley](https://www.shfb.org/)**  
  Services: Free groceries, food pantries  
- **[Sacred Heart Community Service](https://sacredheartcs.org/)**  
  Services: Clothing, food, financial assistance, case management
''')

# ----------------------------------------------------------------
#for legal aid services
st.subheader('Legal Aid', divider= 'blue')
# ----------------------------------------------------------------

# for medical care resources
st.subheader('Medical Care', divider= 'blue')
st.markdown('''
- **[Gardner Health Services](https://gardnerhealthservices.org/)**  
  Services: Primary care, behavioral health, substance use treatment  
- **[Santa Clara Valley Medical Center](https://www.scvmc.org/)**  
  Services: Emergency medical, clinics, urgent care
''')

# for crisis resources
st.subheader('Crisis Lines', divider= 'blue')

col1, col2 = st.columns(2)
with col1:
  st.subheader('Domestic Violence & Safety')
  st.markdown('''
  - **[Next Door Solutions](https://nextdoorsolutions.org/)**  
    24/7 Hotline: (408) 279-2962  
  - **[YWCA Silicon Valley](https://www.ywca-sv.org/)**  
    Services: Safe housing, advocacy, counseling
  ''')
with col2: 
  st.subheader('Mental Health Support')
  st.markdown('''
  - **[988 Suicide & Crisis Lifeline](https://www.988lifeline.org/)**  
    Call/Text: 988 (24/7, Free, Confidential)
  - **[NAMI (National Alliance on Mental Illness)](https://www.nami.org/)**  
    Helpline:  1-800-950-NAMI (6564)
  ''')


col3, col4 = st.columns(2)
with col3:
  st.subheader('Veterans Crisis Line')
  st.markdown('''
  - **[Veterans Crisis Line](https://www.veteranscrisisline.net/)**  
    Call:    Dial 988 then press 1  
    Text:    838255
  ''')
with col4: 
  st.subheader('Human Trafficking Hotline')
  st.markdown('''
  - **[Human Trafficking Hotline](https://www.humantraffickinghotline.org/)**  
    Call:    1-888-373-7888  
    Text:    “HELP” to 233733
  ''')
   


# ----------------------------------------------------------------
# for transportation support
st.subheader('Transportation Support', divider= 'blue')
st.subheader('Local (San Jose / Santa Clara County)')
st.markdown('''
- **VTA Access Paratransit**  
  A shared-ride service for people with disabilities who are unable to use VTA's fixed-route services.  
  Website: https://www.vta.org/access-paratransit (this website does't work anymore)
- **VTA Reduced Fare Clipper Card**  
  Seniors, youth, and people with low income may qualify for discounted public transportation fares.  
  Website: https://www.clippercard.com/ClipperWeb/
- **Destination: Home – Transportation Assistance**  
  Works with service providers to offer transportation vouchers and support as part of homelessness response.  
  Website: https://destinationhomesv.org/
- **Sacred Heart Community Service**  
  Offers case management and can connect individuals with transportation assistance for job interviews, medical appointments, etc.  
  Website: https://www.sacredheartcs.org/
- **LifeMoves** (for referred clients)  
  Sometimes provides limited transportation support like bus passes or shuttle services.  
  Website: https://www.lifemoves.org/
''')
st.subheader('Statewide/National')
st.markdown('''
- **United Way 211**  
  Call 2-1-1 or visit https://www.211.org for help finding transportation services near you based on ZIP code.
- **Catholic Charities of Santa Clara County**  
  Provides transportation help for seniors and low-income families as part of wraparound support.  
  Website: https://www.catholiccharitiesscc.org
- **Non-Emergency Medical Transportation (NEMT)**  
  If you’re a Medi-Cal recipient, you may be eligible for free rides to medical appointments.  
  Info: Call your Medi-Cal managed care provider.
''')
# ----------------------------------------------------------------

# footer
st.markdown("---")
st.caption("Provided by the Sapphire Team 💎 • Powered by OpenAI & Streamlit")