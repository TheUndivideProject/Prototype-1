import streamlit as st
import pandas as pd
import plotly.express as px

# page configuration
st.set_page_config(
    page_title="Corporate SEC Data Dashboard",
    layout="wide",
)

# load SEC data
@st.cache_data
def load_data():
    return pd.read_csv("data/financial-statement-and-notes-2024-modified.csv")

data = load_data()

# page content
st.title("📊 Corporate SEC Data Dashboard")
st.write("Explore corporate financial and operational data from SEC filings.")

## ____________________________________________________________________________________
## key performance indicators (KPIs)

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

# row 1 (number of public companies, number of SICs, median public float)
with st.container():
    col1.metric("Public Companies", data["Name"].nunique(), border=True)
    col2.metric("Standard Industrial Classification (SIC)", data["Standard Industrial Classification (SIC)"].nunique(), border=True)
    col3.metric("Median Public Float", f"${data['Public Float'].median():,.0f}", border=True)

# row 2 (min filing date, max filing Date, median gross profit)
with st.container():
    col4.metric("Minimum Filing Date", data["Date of Filing"].min(), border=True)
    col5.metric("Maximum Filing Date", data["Date of Filing"].max(), border=True)
    col6.metric("Median Gross Profit", f"${data['Gross Profit'].median():,.0f}", border=True)

## ____________________________________________________________________________________
## top reporting metrics

# aggregate number of companies by state 
state_counts = data["State"].value_counts().reset_index()
state_counts.columns = ['State', 'Count']

# create a bar chart for states
state_counts_bar = px.bar(state_counts.head(10),
                          x='State', y='Count',
                          title='Top States by Number of Public Companies',
                          labels={'Count': 'Number of Public Companies', 'State': 'State'},
                          text='Count'
                         )
state_counts_bar.update_traces(texttemplate='%{text}', textposition='outside')

# aggregate number of companies by city
city_counts = data["City"].value_counts().reset_index()
city_counts.columns = ['City', 'Count']

# create a bar chart for cities
city_counts_bar = px.bar(city_counts.head(10),
                          x='City', y='Count',
                          title='Top Cities by Number of Public Companies',
                          labels={'Count': 'Number of Public Companies', 'City': 'City'},
                          text='Count'
                         )
city_counts_bar.update_traces(texttemplate='%{text}', textposition='outside')

# plot both bar charts
col7, col8 = st.columns(2)
col7.plotly_chart(state_counts_bar)
col8.plotly_chart(city_counts_bar)

# aggregate number of companies by sector 
sector_counts = data["Standard Industrial Classification (SIC)"].value_counts().reset_index()
sector_counts.columns = ['Standard Industrial Classification (SIC)', 'Count']

# create a bar chart for sectors
sector_counts_bar = px.bar(sector_counts.head(10),
                          x='Standard Industrial Classification (SIC)', y='Count',
                          title='Top Sectors by Standard Industrial Classification (SIC)',
                          labels={'Count': 'Number of Public Companies', 'Standard Industrial Classification (SIC)': 'Standard Industrial Classification (SIC)'},
                          text='Count'
                         )
sector_counts_bar.update_traces(texttemplate='%{text}', textposition='outside')

# plot sector bar chart
st.plotly_chart(sector_counts_bar)

## ____________________________________________________________________________________
## required detail reporting

# calculate required detail status
detail = (data['Detail'] == 1).sum()
not_detail = data["Name"].nunique() - detail

# create donut chart
required_detail_donut = px.pie(
    names=["At Required Detail Level", "NOT at Required Detail Level"], 
    values=[detail, not_detail], 
    hole=0.5, 
    title="Number of Companies with Schedules at Required Detail Level"
)

# plot donut chart
st.plotly_chart(required_detail_donut)

## ____________________________________________________________________________________
## user-selected metric visualizations

# create a dropdown menu
metric = st.selectbox(
    "I am interested in...",
    ("Accrual for Environmental Loss Contingencies", "Environmental Remediation Expenses", "Charitable Contributions"),
)

with st.container(border=True):

    # key performance indicators (KPIs)
    st.metric(f"Total Corporate {metric} in the U.S.", f"${data[metric].sum():,.0f}", border=True)
    st.metric(f"Median Corporate {metric} in the U.S.", f"${data[metric].median():,.0f}", border=True)
    
    # create a distribution plot
    histogram = px.histogram(data,
                             x=metric,
                             nbins=50,
                             title=f"Distribution of {metric} Among Companies",
                             log_y=True)
    histogram.update_layout(xaxis_title=f"{metric} (USD)", yaxis_title="Frequency (Log Scale)", hovermode="x")

    # calculate reporting status
    not_reporting = data[metric].isnull().sum()
    reporting = data["Name"].nunique() - not_reporting

    # create a donut chart for reporting status
    reporting_donut = px.pie(
        names=["Reporting", "NOT Reporting"], 
        values=[reporting, not_reporting], 
        hole=0.5, 
        title=f"Number of Companies Reporting {metric}",
    )

    # plot distribution and donut chart
    col9, col10 = st.columns(2)
    col9.plotly_chart(histogram)
    col10.plotly_chart(reporting_donut)

    # aggregate metric count by state
    state_totals = data.groupby("State")[metric].agg(Sum="sum", Count="count").reset_index()
    state_totals.columns = ["State", f"Total {metric}", "Number of Companies Reporting"]

    # create a heatmap
    state_totals_choropleth = px.choropleth(state_totals, locations="State", locationmode="USA-states", scope="usa", color=f"Total {metric}", title=f"Total {metric} by State", 
    hover_data={
        "State": True, 
        f"Total {metric}": True, 
        "Number of Companies Reporting": True
    }
)
    # plot heatmap
    state_totals_choropleth.update_traces(marker_line_color='#FFFFFF')
    st.plotly_chart(state_totals_choropleth)
