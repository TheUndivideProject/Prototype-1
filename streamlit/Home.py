import streamlit as st
from PIL import Image

# Set up page configuration
st.set_page_config(
    page_title="SEED: Transparency Dashboards",
    page_icon="🌱",
    layout="wide",
)


# Title and Introducption
st.title("🌱 SEED: Sustainability and Equity Environmental Dashboards")
st.markdown("""
Welcome to SEED, your one-stop platform for philanthropic giving reporting. 
Choose from the dashboard tabs to explore corporate SEC data and nonprofit IRS Form 990 data.
            
This website aims to provide insights into philanthropic spending related to environmental causes by analyzing SEC and IRS data. The goal is to make philanthropic giving data more accessible and understandable, identify the sources of funding, and reveal where and to whom these funds are being directed. This information will be compiled into a dashboard tool to aid donors, communities, and policymakers in making informed decisions about environmental giving.

""")

# Add some spacing between sections
# st.markdown("<br><br>", unsafe_allow_html=True)

# About Each Dashboard (Two Columns)
st.markdown("<h2 style='text-align: center;'> About Each Dashboard </h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 :blue[Corporate Dashboard]")
    st.markdown("""
    Explore corporate giving through our corporate portion of the dashboard. It documents insights from financial and philanthropic metrics from the Securities and Exchange Commission (SEC) financial statements of public companies.
    """)

with col2:
    st.subheader("📋 :green[Nonprofit Dashboard]")
    st.markdown("""
    Navigate current nonprofit spending through our nonprofit dashboard documents. This includes insights from financial and philanthropic metrics from the IRS Exempt Organizations Business Master File and Form 990 filings of tax-exempt organizations.
    """)


with st.expander("🌱 More About SEED 🌱"):
    st.markdown("""
                
    Transparency is our number one goal. Although current data is accessible via the SEC and IRS, the breadth and depth of this data makes it extremely difficult for those at large without much data science experience to analyze accountability of how philanthropic giving operates in cities of interest and whether this philanthropic giving is reported. This guts the ideal of a feedback loop between the donors that are giving, and the impacted communities that are supposed to receive assistance.

    Thus, our objective is to re-establish this feedback loop between communities and philanthropic giving officers, ensuring that the perspectives and leadership of community members are at the forefront of all funding decisions.

    This will start as comparative analysis of Corporations and Nonprofits. This will be done through documents provided by the Securities and Exchange Commission (SEC) and the IRS (through their Business Master File and Form 990s). *More information on these will be provided in their respective analyses*. As a result, it will lay the foundation for trend analysis, and where we project this giving to be in the future.

    Utlimately, this will operate as a multi-faceted tool that combines education, transparency, and decision-making. Through the education of communities at large, we can find accoutnability and decision-making for government agencies involved not only to make sure impacted communities are served, but to hold those accountable for their philanthropic giving. This innovative dashboard will serve as a convenient platform for direct verification of funding impacts, empowering communities to track and assess the resources flowing into their areas.

                """)

###################
# SIDEBAR CONTENT #
###################

def read_logos(logos_path):
    """
    Reads and returns the STC, UNICEF, and DSA logos from the provided path.

    Parameters:
    -----------
    logos_path : str
        The path to the directory containing the logo images.

    Returns:
    --------
    tuple of PIL.Image.Image
        The STC, UNICEF, and DSA logos as PIL Image objects.
    """
    TUPLogo = Image.open(f"{logos_path}/TUP_logo.png")
    return TUPLogo

# Image
TUPLogo = read_logos("pictures")
st.sidebar.image(TUPLogo)

# TUP Overview Dropdown
with st.sidebar.expander("About TUP"):
    st.markdown("""
    The Undivide Project focuses on the intersection of the climate crisis and the digital divide. 
    We are most concerned about how the confluence of these critical issues impacts poor and BIPOC communities. 
    Our goal is to use a portfolio of services to help communities create their own solutions. 
    And we always — always unapologetically uplift the voices of the underserved.
    """)
