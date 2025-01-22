import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Corporate SEC Data Dashboard",
    layout="wide",
)

# Load SEC data
# @st.cache_data
# def load_sec_data():
#     return pd.read_csv("data/sec_data.csv")

# sec_data = load_sec_data()

# Page content
st.title("📊 Corporate SEC Data Dashboard")
st.markdown("""
Analyze corporate financial disclosures from SEC filings.
""")


# # Select key metrics for visualization
# st.subheader("Visualization")
# metric = st.selectbox("Select a metric to analyze:", sec_data.columns)

# if metric:
#     st.write(f"### {metric} Over Time")
#     fig, ax = plt.subplots()
#     sec_data.groupby("Year")[metric].sum().plot(kind="line", ax=ax)
#     st.pyplot(fig)
