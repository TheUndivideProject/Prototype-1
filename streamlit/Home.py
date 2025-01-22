import streamlit as st

# Set up page configuration
st.set_page_config(
    page_title="SEED: Transparency Dashboards",
    page_icon="🌱",
    layout="wide",
)

# Title and Introduction
st.title("🌱 SEED: Sustainability and Equity Environmental Dashboards")
st.markdown("""
Welcome to SEED, your one-stop platform for transparency and impact reporting. 
Choose from the dashboards below to explore corporate SEC data and nonprofit IRS Form 990 data.
""")



# Side Bar Set Up
st.sidebar.markdown(
        """
        <style>
            [data-testid="stVerticalBlock"] > img:first-child {
                margin-top: -60px;
            }

            [data-testid=stImage]{
                text-align: center;
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 100%;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
# Add Sidebar image and Text
st.sidebar.title("Navigation")
st.sidebar.markdown("Select a page to view:")
page = st.sidebar.radio("Pages", ["Corporate SEC Dashboard", "Nonprofit IRS Dashboard"])



# Load selected page
if page == "Corporate SEC Dashboard":
    st.experimental_rerun()  # Redirect to the Corporate SEC page
elif page == "Nonprofit IRS Dashboard":
    st.experimental_rerun()  # Redirect to the Nonprofit IRS page
