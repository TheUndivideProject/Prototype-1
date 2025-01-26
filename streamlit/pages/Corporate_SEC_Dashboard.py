import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# page configuration
st.set_page_config(
    page_title="Corporate SEC Data Dashboard",
    layout="wide",
)

# load SEC data
@st.cache_data
def load_sec_data():
    return pd.read_csv("../data/financial-statement-and-notes-2024-modified.csv")

sec_data = load_sec_data()

# page content
st.title("📊 Corporate SEC Data Dashboard")
st.write("Explore corporate financial and operational data from SEC filings.")

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

with st.container():
    col1.metric("Registrants", sec_data["Name"].nunique(), border=True)
    col2.metric("Standard Industrial Classification (SIC)", sec_data["Standard Industrial Classification (SIC)"].nunique(), border=True)
    col3.metric("Median Pubilc Float", f"${sec_data['Public Float'].median():,.0f}", border=True)

with st.container():
    col4.metric("Minimum Filing Date", sec_data["Date of Filing"].min(), border=True)
    col5.metric("Maximum Filing Date", sec_data["Date of Filing"].max(), border=True)
    col6.metric("Median Gross Profit", f"${sec_data['Gross Profit'].median():,.0f}", border=True)
