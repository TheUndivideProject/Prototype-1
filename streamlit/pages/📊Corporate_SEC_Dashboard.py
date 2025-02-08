import streamlit as st
import pandas as pd
import plotly.express as px
from us import states

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
st.write("Explore corporate financial and operational data from 10-Ks, 10-Ws, earnings releases, proxy statements, 8-Ks, and comment letters filed with the SEC in 2024.")

## ____________________________________________________________________________________
## filer profile

# title for the section
st.header("Who's Represented in the Data?")

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

# row 1 (number of public companies, number of SICs, median public float)
with st.container():
    col1.metric("Public Companies", data["Name"].nunique(), border=True)
    col2.metric("Standard Industrial Classification (SIC)", data["Standard Industrial Classification (SIC)"].nunique(), border=True, help="SICs are three or four-digit numerical codes that categorize the industries that companies belong to based on their business activities (e.g. '6500' for Real Estate).")
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

# create a bar chart for top states
state_counts_bar = px.bar(state_counts.head(3),
                          x='Count', y='State',
                          title='Top 3 States by Number of Corporate Headquarters',
                          labels={'Count': 'Number of Corporate Headquarters', 'State': 'State'},
                          text='Count',
                          orientation='h'
                         )
state_counts_bar.update_traces(texttemplate='%{text}', textposition='outside')

# aggregate number of companies by city
city_counts = data["City"].value_counts().reset_index()
city_counts.columns = ['City', 'Count']

# create a bar chart for top cities
city_counts_top_bar = px.bar(city_counts.head(10),
                              x='Count', y='City',
                              title='Top 10 Cities by Number of Corporate Headquarters',
                              labels={'Count': 'Number of Corporate Headquarters', 'City': 'City'},
                              text='Count',
                              orientation='h'
                             )
city_counts_top_bar.update_traces(texttemplate='%{text}', textposition='outside')

# plot both bar charts
col7, col8 = st.columns(2)
col7.plotly_chart(state_counts_bar)
col8.plotly_chart(city_counts_top_bar)

# expand top 3 state names
top_state1 = states.lookup(state_counts.iloc[0]['State']).name
top_state2 = states.lookup(state_counts.iloc[1]['State']).name
top_state3 = states.lookup(state_counts.iloc[2]['State']).name

top_city1 = city_counts.iloc[0]['City'].title()
top_city2 = city_counts.iloc[1]['City'].title()
top_city3 = city_counts.iloc[2]['City'].title()

# add context
col7.markdown(f"**{top_state1}**, **{top_state2}**, and **{top_state3}** are the three states with the **highest** number of corporate headquarters. These headquarters can increase the number of high-income earners in the state, resulting in **more direct donations** to charitable organizations (Card, Hallock, & Moretti, 2009).")
col8.markdown(f"**{top_city1}**, **{top_city2}**, and **{top_city3}** are the three cities with the **highest** number of corporate headquarters. These headquarters can increase the number of high-income earners in the state, resulting in **more direct donations** to charitable organizations (Card, Hallock, & Moretti, 2009).")

# will visualize the bottom X cities here once I receive feedback from the team.

# create a bar chart for bottom states
state_counts_bottom_bar = px.bar(state_counts.tail(3),
                          x='Count', y='State',
                          title='Bottom 3 States by Number of Corporate Headquarters',
                          labels={'Count': 'Number of Corporate Headquarters', 'State': 'State'},
                          text='Count',
                          orientation='h'
                         )
state_counts_bottom_bar.update_traces(texttemplate='%{text}', textposition='outside')

# plot bar chart
col9, col10 = st.columns(2)
col7.plotly_chart(state_counts_bottom_bar)

# expand bottom 3 state names
bottom_state1 = states.lookup(state_counts.iloc[-3]['State']).name
bottom_state2 = states.lookup(state_counts.iloc[-2]['State']).name
bottom_state3 = states.lookup(state_counts.iloc[-1]['State']).name

# add context
col7.markdown(f"**{bottom_state1}**, **{bottom_state2}**, and **{bottom_state3}** are the three states with the **lowest** number of corporate headquarters. The lack of headquarters can limit the number of high-income earners in the state, resulting in **fewer direct donations** to charitable organizations (Card, Hallock, & Moretti, 2009).")

# aggregate number of companies by sector 
sector_counts = data["Standard Industrial Classification (SIC)"].value_counts().reset_index()
sector_counts.columns = ['Standard Industrial Classification (SIC)', 'Count']

# create a bar chart for sectors
sector_counts_bar = px.bar(sector_counts.head(10),
                          x='Standard Industrial Classification (SIC)', y='Count',
                          title='Top 10 Sectors by Standard Industrial Classifications (SICs)',
                          labels={'Count': 'Number of Public Companies', 'Standard Industrial Classification (SIC)': 'Standard Industrial Classification (SIC)'},
                          text='Count',
                         )
sector_counts_bar.update_traces(texttemplate='%{text}', textposition='outside')

# plot sector bar chart
st.plotly_chart(sector_counts_bar)

top_sector1 = int(sector_counts.iloc[0]['Standard Industrial Classification (SIC)'])
top_sector2 = int(sector_counts.iloc[1]['Standard Industrial Classification (SIC)'])
top_sector3 = int(sector_counts.iloc[3]['Standard Industrial Classification (SIC)'])

# add context
st.markdown(f"SICs are three or four-digit numerical codes that categorize the industries that companies belong to based on their business activities. The three **most represented** sectors in this dataset are **Pharmaceutical Preparations** ({top_sector1}), **Real Estate Investment Trusts** ({top_sector2}), and **Blank Checks** ({top_sector3}).")
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
# add context
st.markdown(f"A submission “at Required Detail Level” includes detailed quantitative disclosures in its footnotes and schedules. For example, rather than a total expense figure, it breaks down amounts into categories like compensation, accounting fees, and legal fees. Most submissions **do not** meet this level of detail ({(not_detail / (not_detail + detail) * 100):.1f}%).")

## ____________________________________________________________________________________
## user-selected metric visualizations

# title for the section
st.header("What Does the Data Reveal About Spending on Environmental and Social Justice Causes?")

# create a dropdown menu
metric = st.selectbox(
    "Select a metric:",
    ("Accrual for Environmental Loss Contingencies", "Environmental Remediation Expenses", "Charitable Contributions"),
)

with st.container(border=True):

    st.subheader(metric)

    # add context
    if metric == 'Accrual for Environmental Loss Contingencies':
        st.markdown("This refers to *unspent* funds set aside for potential *future* environmental damages.")
    elif metric == 'Environmental Remediation Expenses':
        st.markdown("This refers to funds *spent* on the cleanup or restoration of environmental damages.")
    else:
        st.markdown("This refers to funds *donated* to support charitable causes or nonprofit organizations.")

    st.metric(f"Total {metric}", f"${data[metric].sum():,.0f}", border=True)
    st.metric(f"Median {metric}", f"${data[metric].median():,.0f}", border=True)
    
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
