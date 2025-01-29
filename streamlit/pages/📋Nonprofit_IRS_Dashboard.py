import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
# import pydeck as pdk

# Page configuration
st.set_page_config(
    page_title="📋Nonprofit IRS Form 990 Data Dashboard",
    layout="wide",
)


# Page content
st.title("Nonprofit IRS Form 990 Data Dashboard")
st.markdown("""
Explore nonprofit financial and operational data from IRS Form 990 filings.
""")


# Cache the data loading for better performance
@st.cache_data
def load_data(filepath):
    return pd.read_csv(filepath)

# Define the path to the dataset
data_path = "../data/Updated Regional Giving Data IRS eo1.csv"

# Load the data
data = load_data(data_path)



### Top Reporting
# Aggregate revenue by state
state_funding = data.groupby('STATE')['REVENUE_AMT'].sum().reset_index()
state_funding.columns = ['State', 'Total Revenue']

# Sort data to get top 10 and bottom 10 states
top_3_states = state_funding.sort_values(by='Total Revenue', ascending=False).head(3)
bottom_3_states = state_funding.sort_values(by='Total Revenue', ascending=True).head(3)

# Title for the section
st.header("Funding Distribution by State")

# Top 3 States
st.subheader("🌟 Top 3 States by Funding")
st.markdown("""
These states are receiving the highest levels of nonprofit funding. This could indicate areas with greater philanthropic activity or larger nonprofit networks.
""")
fig_top = px.bar(top_3_states, 
                 x='Total Revenue', y='State', 
                 orientation='h', 
                 title='Top 3 States by Total Revenue',
                 labels={'Total Revenue': 'Total Revenue (USD)', 'State': 'State'},
                 text='Total Revenue',
                 color='Total Revenue',
                 color_continuous_scale='greens')

fig_top.update_traces(texttemplate='$%{text:.2s}', textposition='outside')
fig_top.update_layout(xaxis_title='Total Revenue (USD)', yaxis_title='State')
st.plotly_chart(fig_top)

# Bottom 3 States
st.subheader("🔍 Bottom 3 States by Funding")
st.markdown("""
These states have the lowest levels of nonprofit funding. They may represent underserved regions or areas of potential investment for philanthropic organizations.
""")
fig_bottom = px.bar(bottom_3_states, 
                    x='Total Revenue', y='State', 
                    orientation='h', 
                    title='Bottom 3 States by Total Revenue',
                    labels={'Total Revenue': 'Total Revenue (USD)', 'State': 'State'},
                    text='Total Revenue',
                    color='Total Revenue',
                    color_continuous_scale='reds')

fig_bottom.update_traces(texttemplate='$%{text:.2s}', textposition='outside')
fig_bottom.update_layout(xaxis_title='Total Revenue (USD)', yaxis_title='State')
st.plotly_chart(fig_bottom)


### State Choropleth
# Aggregate total revenue by state
state_funding = data.groupby('STATE')['REVENUE_AMT'].sum().reset_index()
state_funding.columns = ['State', 'Total Revenue']

# Create a heatmap
fig = px.choropleth(state_funding, 
                    locations='State', 
                    locationmode='USA-states', 
                    color='Total Revenue',
                    color_continuous_scale='Viridis',
                    scope='usa',
                    title='Funding Distribution Across States')
st.plotly_chart(fig)


# Aggregate funding by NTEE_CD
sector_funding = data.groupby('NTEE_CD')['REVENUE_AMT'].sum().reset_index()
sector_funding.columns = ['Sector (NTEE_CD)', 'Total Revenue']

# Calculate compliance status
compliance_status = data['FILING_REQ_CD'].value_counts().reset_index()
compliance_status.columns = ['Compliance Status', 'Count']

# Create a pie chart
fig = px.pie(compliance_status, 
             names='Compliance Status', 
             values='Count',
             title='Compliance Status of Nonprofits')
st.plotly_chart(fig)


# # Generate points map for nonprofits
# layer = pdk.Layer(
#     "ScatterplotLayer",
#     data=data,
#     get_position="[longitude_column, latitude_column]",  # Replace with actual columns
#     get_radius=500,
#     get_color=[200, 30, 0, 160],
#     pickable=True,
# )

# view_state = pdk.ViewState(latitude=37.7749, longitude=-122.4194, zoom=3)  # Adjust to USA
# st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

### Visualization 1: Interactive Top States by # of Nonprofits
# Top States by Number of Nonprofits
state_counts = data['STATE'].value_counts().reset_index()
state_counts.columns = ['State', 'Count']

# Interactive Bar Chart
fig_states = px.bar(state_counts.head(10), 
                    x='State', y='Count', 
                    title='Top States by Number of Nonprofits',
                    labels={'Count': 'Number of Nonprofits'},
                    text='Count')

fig_states.update_traces(texttemplate='%{text}', textposition='outside')
fig_states.update_layout(xaxis_title='State', yaxis_title='Count of Nonprofits',
                         showlegend=False)

st.plotly_chart(fig_states)


### Visualization 2: Revenue
# Revenue Distribution
fig_revenue = px.histogram(data, 
                           x='REVENUE_AMT', 
                           nbins=50, 
                           title='Distribution of Revenue Among Nonprofits',
                           labels={'REVENUE_AMT': 'Revenue Amount'},
                           log_y=True)

fig_revenue.update_layout(xaxis_title='Revenue Amount (USD)', 
                          yaxis_title='Frequency (Log Scale)',
                          hovermode='x')

st.plotly_chart(fig_revenue)

# Add context
st.markdown("**Note**: Most nonprofits have lower revenue, but there are some high-revenue outliers that significantly impact the overall distribution.")


# Top Sectors by Activity Code
sector_counts = data['NTEE_CD'].value_counts().reset_index()
sector_counts.columns = ['Activity Code', 'Count']

fig_sectors = px.bar(sector_counts.head(10), 
                     x='Activity Code', y='Count', 
                     title='Top Sectors by Activity Code (NTEE_CD)',
                     labels={'Count': 'Number of Nonprofits', 'Activity Code': 'NTEE Code'},
                     text='Count')

fig_sectors.update_traces(texttemplate='%{text}', textposition='outside')
fig_sectors.update_layout(xaxis_title='Activity Code (NTEE_CD)', yaxis_title='Count of Nonprofits')

st.plotly_chart(fig_sectors)

# Add context
st.markdown("**Note**: Each NTEE Code represents a specific nonprofit activity type (e.g., 'X20' for Religion-related services).")



# # Select key metrics for visualization
# st.subheader("Visualization")
# metric = st.selectbox("Select a metric to analyze:", irs_data.columns)

# if metric:
#     st.write(f"### {metric} Distribution")
#     fig, ax = plt.subplots()
#     irs_data[metric].hist(bins=20, ax=ax)
#     st.pyplot(fig)



