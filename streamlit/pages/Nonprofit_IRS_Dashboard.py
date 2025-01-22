import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Nonprofit IRS Form 990 Data Dashboard",
    layout="wide",
)

# # Load IRS data
# @st.cache_data
# def load_irs_data():
#     return pd.read_csv("data/irs_data.csv")

# irs_data = load_irs_data()

# Page content
st.title("📋 Nonprofit IRS Form 990 Data Dashboard")
st.markdown("""
Explore nonprofit financial and operational data from IRS Form 990 filings.
""")


# # Select key metrics for visualization
# st.subheader("Visualization")
# metric = st.selectbox("Select a metric to analyze:", irs_data.columns)

# if metric:
#     st.write(f"### {metric} Distribution")
#     fig, ax = plt.subplots()
#     irs_data[metric].hist(bins=20, ax=ax)
#     st.pyplot(fig)
