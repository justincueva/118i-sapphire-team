import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="EIH Budget Allocation", layout="wide")
st.title("💰 Budget & Financial Planning for Emergency Interim Housing")
st.caption("Breakdown of costs, funding sources, and what’s needed to scale.")

st.markdown("---")

st.header("📊 Current Year Budget Overview (Sample)")

budget_data = {
    'Category': ['Facility Leasing', 'Staff Wages', 'Food & Supplies', 'Mental Health Services', 'Security', 'Transportation', 'Admin & Overhead'],
    'Cost ($)': [1200000, 850000, 500000, 400000, 200000, 150000, 100000]
}
df = pd.DataFrame(budget_data)

st.dataframe(df)

st.subheader("💸 Total Annual Budget")
total_budget = df["Cost ($)"].sum()
st.metric(label="Projected Budget", value=f"${total_budget:,}")

st.markdown("---")
st.header("📉 Budget Allocation Chart")
fig, ax = plt.subplots()
ax.pie(df["Cost ($)"], labels=df["Category"], autopct="%1.1f%%", startangle=140)
ax.axis("equal")
st.pyplot(fig)

st.markdown("---")
st.header("💬 Funding Sources")

sources = {
    "Federal HUD Grants": "$1,000,000",
    "State Emergency Funds": "$800,000",
    "City Budget Allocation": "$600,000",
    "Private/Philanthropy": "$300,000"
}
for key, val in sources.items():
    st.markdown(f"- **{key}**: {val}")

st.markdown("---")
st.header("🧮 Budget Gap Analysis")

gap = total_budget - (1000000 + 800000 + 600000 + 300000)
if gap <= 0:
    st.success("✅ Fully funded! Great job building strong partnerships.")
else:
    st.error(f"🚨 Budget shortfall: ${gap:,}.")
    st.markdown("""
    **Recommendations**:
    - Apply for FEMA Transitional Shelter Assistance  
    - Launch community donor campaign  
    - Reduce admin costs via shared service models  
    """)

st.markdown("---")
st.caption("Note: All numbers are illustrative and for prototype purposes.")
