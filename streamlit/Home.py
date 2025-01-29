import streamlit as st
import matplotlib.pyplot as plt

# Set up page configuration
st.set_page_config(
    page_title="SEED: Transparency Dashboards",
    page_icon="🌱",
    layout="wide",
)

# Title and Introducption
st.title("🌱 SEED: Sustainability and Equity Environmental Dashboards")
st.markdown("""
Welcome to SEED, your one-stop platform for transparency and impact reporting. 
Choose from the dashboards to explore corporate SEC data and nonprofit IRS Form 990 data.
""")

st.header("About Us")

st.markdown("""
            
This website aims to provide insights into philanthropic spending related to environmental causes by analyzing SEC and IRS data. The goal is to make philanthropic giving data more accessible and understandable, identify the sources of funding, and reveal where and to whom these funds are being directed. This information will be compiled into a dashboard tool to aid donors, communities, and policymakers in making informed decisions about environmental giving.

Transparency is our number one goal. Although current data is accessible via the SEC and IRS, the breadth and depth of this data makes it extremely difficult for those at large without much data science experience to analyze accountability of how philanthropic giving operates in cities of interest and whether this philanthropic giving is reported. This guts the ideal of a feedback loop between the donors that are giving, and the impacted communities that are supposed to receive assistance.

Thus, our objective is to reestablish this feedback loop between communities and philanthropic giving officers, ensuring that the perspectives and leadership of community members are at the forefront of all funding decisions.

This will start as comparative analysis of Corporations and Nonprofits. This will be done through documents provided by the Securities and Exchange Commission (SEC) and the IRS (through their Business Master File and Form 990s). *More information on these will be provided in their respective analyses*. As a result, it will lay the foundation for trend analysis, and where we project this giving to be in the future.

Utlimately, this will operate as a multi-faceted tool that combines education, transparency, and decision-making. Through the education of communities at large, we can find accoutnability and decision-making for government agencies involved not only to make sure impacted communities are served, but to hold those accountable for their philanthropic giving. This innovative dashboard will serve as a convenient platform for direct verification of funding impacts, empowering communities to track and assess the resources flowing into their areas.

            """)


st.header("About Each Dashboard")
st.markdown("""
-   **Corporate**: documents insights from financial and philanthropic metrics from the Securities and Exchange Commission (SEC) financial statements of public companies.

-   **Nonprofit**: documents insights from financial and philanthropic metrics from the IRS Exempt Organizations Business Master File and Form 990 filings of tax-exempt organizations.

-   **Comparative Analysis**: This page will highlight a comparative analysis of the individual work done on the Corporate and Nonprofit level. It will provide both a holistic view of how philanthropic giving operates at different granularities, and be the starting point for our dashboard.
            """)


st.header("Current Actionable Insights")

st.markdown("Input some actionable insights from both of the dashboards together? ")


st.markdown("*Insert an about the data, logo, and TUP dropdown")


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




  
# # Add Sidebar image and Text
# st.sidebar.title("Navigation")
# st.sidebar.markdown("Select a page to view:")
# page = st.sidebar.radio("Pages", ["Corporate SEC Dashboard", "Nonprofit IRS Dashboard"])




# # Load selected page
# if page == "Corporate SEC Dashboard":
#     st.experimental_rerun()  # Redirect to the Corporate SEC page
# elif page == "Nonprofit IRS Dashboard":
#     st.experimental_rerun()  # Redirect to the Nonprofit IRS page
