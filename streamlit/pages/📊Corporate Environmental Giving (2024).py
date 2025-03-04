import pandas as pd
import streamlit as st
import plotly.express as px
from scipy.stats import skew
from us import states
from scipy.stats import skew
import folium
from folium import plugins
from Home import read_logos

# configure page
st.set_page_config(
    page_title="📊 Corporate Environmental Giving (2024)",
    layout="wide"
)

# load SEC Financial Statement and Notes data (https://www.sec.gov/data-research/sec-markets-data/financial-statement-notes-data-sets)
@st.cache_data
def load_data():
    return pd.read_csv("data/financial-statement-and-notes-2024-modified.csv")
data = load_data()

# set page title
st.title("📊 Corporate Environmental Giving (2024)")

####################################
#        SUMMARY STATISTICS        #
####################################

# set section title
st.header("Who's Represented in the Data?")

def compute_summary_statistics(data):
    # Compute the necessary metrics
    companies = data["Name"].nunique()
    SICs = data["Standard Industrial Classification (SIC)"].nunique()
    median_float = f"${data['Public Float'].median():,.0f}"
    min_filing_date = data["Date of Filing"].min()
    max_filing_date = data["Date of Filing"].max()
    median_gross_profit = f"${data['Gross Profit'].median():,.0f}"

    return {
        "Public Companies": companies,
        "Standard Industrial Classifications (SICs)": SICs,
        "Median Public Float": median_float,
        "Minimum Filing Date": min_filing_date,
        "Maximum Filing Date": max_filing_date,
        "Median Gross Profit": median_gross_profit,
    }

# compute summary statistics
summary_statistics = compute_summary_statistics(data)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Public Companies", value=f"{summary_statistics['Public Companies']:,}", border=True)

with col2:
    st.metric(label="Standard Industrial Classifications (SICs)", value=f"{summary_statistics['Standard Industrial Classifications (SICs)']:,}", border=True)

with col3:
    st.metric(label="Median Public Float", value=summary_statistics['Median Public Float'], border=True)

col4, col5, col6 = st.columns(3)
with col4:
    st.metric(label="Minimum Filing Date", value=str(summary_statistics['Minimum Filing Date']), border=True)

with col5:
    st.metric(label="Maximum Filing Date", value=str(summary_statistics['Maximum Filing Date']), border=True)

with col6:
    st.metric(label="Median Gross Profit", value=summary_statistics['Median Gross Profit'], border=True)

####################################
#          ABOUT THE DATA          #
####################################

with st.expander("📖 About the Data"):
    st.markdown(
        """
        ## 🗂 Data Sources & Importance
        This dashboard tracks corporate spending on environmental and social justice causes using information from all financial statements (Form 10-Ks, Form 10-Qs, Earnings Releases, Form 8-Ks, etc.) filed with the SEC in 2024.
        
        **1️⃣ Financial Statement and Notes Submission Data Set**  
        - **What it is**: A dataset containing all SEC-registered companies.
        - **Why it matters**: Provides insights into active companies, their locations, and the level of detail in their financial reports.
        - **More info**: [SEC Financial Statement and Notes Data Sets](https://www.sec.gov/data-research/sec-markets-data/financial-statement-notes-data-sets)
        
        **2️⃣ Financial Statement and Notes Numeric Data Set**  
        - **What it is**: A dataset containing numeric data from SEC-registered companies' filings, including detailed figures from financial statements and notes.
        - **Why it matters**: Provides insights into revenue, environmental loss contingencies, and charitable contributions.
        - **More info**: [SEC Financial Statement and Notes Data Sets](https://www.sec.gov/data-research/sec-markets-data/financial-statement-notes-data-sets)
        """
    )

#####################################################
#  WHO'S REPRESENTED IN THE DATA? (SPECIFIC CHARTS) #
#####################################################

def plot_charts(num_columns, charts, contexts):
    columns = st.columns(num_columns)
    for column, chart, context in zip(columns, charts, contexts):
        column.plotly_chart(chart)
        column.markdown(context)

### top reporting

# aggregate number of headquarters by state
state_headquarter_counts = data["State"].value_counts().reset_index()
state_headquarter_counts.columns = ["State", "Count"]

# create a bar chart for the top 3 states
top_state_headquarter_counts = state_headquarter_counts.head(3)
top_state_headquarter_counts_bar = px.bar(top_state_headquarter_counts,
                                          x="Count", y="State",
                                          title="Top 3 States by Number of Corporate Headquarters",
                                          labels={"Count": "Number of Corporate Headquarters", "State": "State"},
                                          orientation="h"
                                          )
# add context
top_state_headquarter_count1 = states.lookup(top_state_headquarter_counts.iloc[0]['State']).name
top_state_headquarter_count2 = states.lookup(top_state_headquarter_counts.iloc[1]['State']).name
top_state_headquarter_count3 = states.lookup(top_state_headquarter_counts.iloc[2]['State']).name
top_state_headquarter_counts_context = f"**{top_state_headquarter_count1}**, **{top_state_headquarter_count2}**, and **{top_state_headquarter_count3}** were the three states with the **highest** number of corporate headquarters. These headquarters can increase the number of high-income earners in the state, resulting in **more direct donations** to charitable organizations (Card, Hallock, & Moretti, 2009)."

# create a bar chart for the bottom 3 states
bottom_state_headquarter_counts = state_headquarter_counts.tail(3)
bottom_state_headquarter_counts_bar = px.bar(bottom_state_headquarter_counts,
                                          x="Count", y="State",
                                          title="Bottom 3 States by Number of Corporate Headquarters",
                                          labels={"Count": "Number of Corporate Headquarters", "State": "State"},
                                          orientation="h"
                                          )
# add context
bottom_state_headquarter_count1 = states.lookup(bottom_state_headquarter_counts.iloc[-1]['State']).name
bottom_state_headquarter_count2 = states.lookup(bottom_state_headquarter_counts.iloc[-2]['State']).name
bottom_state_headquarter_count3 = states.lookup(bottom_state_headquarter_counts.iloc[-3]['State']).name
bottom_state_headquarter_counts_context = f"**{bottom_state_headquarter_count1}**, **{bottom_state_headquarter_count2}**, and **{bottom_state_headquarter_count3}** were the three states with the **lowest** number of corporate headquarters. The lack of headquarters can limit the number of high-income earners in the state, resulting in **fewer direct donations** to charitable organizations (Card, Hallock, & Moretti, 2009)."
        
# plot top and bottom 3 states in 2 columns
plot_charts(2, [top_state_headquarter_counts_bar, bottom_state_headquarter_counts_bar], [top_state_headquarter_counts_context, bottom_state_headquarter_counts_context])

# aggregate number of companies by sector
sector_counts = data["Standard Industrial Classification (SIC)"].value_counts().reset_index()
sector_counts.columns = ["Standard Industrial Classification (SIC)", "Count"]

# create a bar chart for the top 3 sectors
top_sector_counts = sector_counts.head(10)
top_sector_counts_bar = px.bar(top_sector_counts,
                                          x="Standard Industrial Classification (SIC)", y="Count",
                                          title="Top 10 Sectors by Standard Industrial Classification (SIC)",
                                          labels={"Count": "Number of Public Companies", "Standard Industrial Classification (SIC)": "Standard Industrial Classification (SIC)"}
                                          )
top_sector_counts_bar.update_layout(xaxis=dict(type="category"))

# add context
top_sector_count1 = int(top_sector_counts.iloc[0]['Standard Industrial Classification (SIC)'])
top_sector_count2 = int(top_sector_counts.iloc[1]['Standard Industrial Classification (SIC)'])
top_sector_count3 = int(top_sector_counts.iloc[2]['Standard Industrial Classification (SIC)'])
top_sector_counts_context = f"Standard Industrial Classifications (SICs) are three or four-digit numerical codes that categorize the industries that companies belong to based on their business activities (e.g. '1311' for Crude Petroleum and Natural Gas). The three **most represented** sectors were **Pharmaceutical Preparations** ({top_sector_count1}, **Real Estate Investment Trusts** ({top_sector_count2}), and **Blank Checks** ({top_sector_count3})."

# plot top sectors
plot_charts(1, [top_sector_counts_bar], [top_sector_counts_context])

### detail reporting

# calculate detail status
at_detail = (data['Detail'] == 1).sum()
not_at_detail = data["Name"].nunique() - at_detail

# create a donut chart for detail status
detail_counts_donut = px.pie(
    names=["At Required Detail Level", "NOT at Required Detail Level"],
    values=[at_detail, not_at_detail],
    title="Number of Public Companies with Schedules at Required Detail Level",
    hole=0.5
)
# add context
detail_counts_donut_context = f"A submission “at Required Detail Level” includes detailed quantitative disclosures in its footnotes and schedules. For example, instead of a total expense figure, it breaks down amounts into categories like compensation, accounting fees, and legal fees. Most submissions **did not** meet this level of detail ({(not_at_detail / (not_at_detail + at_detail) * 100):.1f}%). This could suggest **incomplete** and/or **inconsistent** philanthropic reports."

# plot detail status
plot_charts(1, [detail_counts_donut], [detail_counts_donut_context])

#####################################################
#   WHAT DOES THE DATA REVEAL... (SPECIFIC CHARTS)  #
#####################################################

# set section title
st.header("What Does the Data Reveal About Spending on Environmental and Social Justice Causes?")

### filters

col1, col2 = st.columns(2)

# filter data based on the selected metric
metrics = {
    'Accrual for Environmental Loss Contingencies': f"are unspent funds set aside for potential future environmental damages.",
    'Environmental Remediation Expenses': "are funds spent on the cleanup or restoration of environmental damages.",
    'Charitable Contributions': "are funds donated to support charitable causes or nonprofit organizations."
}
metric = col1.selectbox("Select a metric:", metrics.keys())
metric_data = data[data[metric].notna()]

# filter data based on the selected state
state = col2.selectbox(
    "Select a state (or \"None\" for the entire U.S.):",
    ["None"] + list(metric_data[metric_data[metric].notna()]["State"].unique())
)
if state != "None":
    metric_data = metric_data[metric_data['State'] == state]
    st.subheader(f"{metric} in {states.lookup(state).name}", help=f"{metric} {metrics.get(metric)}")
else: 
    st.subheader(f"{metric}", help=f"{metric} {metrics.get(metric)}")

# present metric total and median
col1, col2 = st.columns(2)

metric_total = f"${metric_data[metric].sum():,.0f}"
metric_median = f"${metric_data[metric].median():,.0f}"

col1.metric(f"Total {metric}", metric_total, border=True)
col2.metric(f"Median {metric}", metric_median, border=True)

### metric distribution

metric_distribution = px.histogram(metric_data,
                         x=metric,
                         nbins=50,
                         title=f"Distribution of {metric} Among Public Companies",
                         log_y=True
                         )
metric_distribution.update_layout(xaxis_title=f"{metric} (USD)", yaxis_title="Frequency (Log Scale)", hovermode="x")

# add context
metric_skewness = skew(metric_data[metric], axis=0, bias=True)

if metric_skewness > 0:
    metric_skewness = "right-skewed"
elif metric_skewness < 0:
    metric_skewness = "left-skewed"
else:
    metric_skewness = "Normal"

metric_distribution_context = f"The distribution of {metric} is **{metric_skewness}** with a median of **\{metric_median}**. Most {metric} fell in the range of **\${metric_data[metric].quantile(.25):,.0f}-${metric_data[metric].quantile(.75):,.0f}**."

# calculate reporting status
reporting_metric = metric_data["Name"].nunique()
not_reporting_metric = data["Name"].nunique() - reporting_metric

# create a donut chart for reporting status
metric_reporting_counts_donut = px.pie(
    names=[f"Reporting {metric}", f"NOT Reporting {metric}"],
    values=[reporting_metric, not_reporting_metric],
    title=f"Number of Public Companies Reporting {metric}",
    hole=0.5
)

# add context
metric_reporting_counts_context = f"Most public companies **did not** report {metric} ({(not_reporting_metric / (not_reporting_metric + reporting_metric) * 100):.1f}%). This could suggest **incomplete** and/or **inconsistent** philanthropic reports."

# plot distribution and donut chart in 2 columns
plot_charts(2, [metric_distribution, metric_reporting_counts_donut], [metric_distribution_context, metric_reporting_counts_context])

if state != "None":
    # get coordinates of selected state
    state_coordinates = pd.read_csv("data/state-coordinates.csv")
    state_latitude, state_longitude = state_coordinates[state_coordinates["State"] == state][["Latitude", "Longitude"]].values[0]

    # create a map of companies reporting 'metric', centered on the selected state
    metric_reporting_counts_map = folium.Map(location=[state_latitude, state_longitude], zoom_start = 7, min_zoom = 5)
    marker_cluster = plugins.MarkerCluster().add_to(metric_reporting_counts_map)
    for row in metric_data.itertuples(index=False):
        if pd.notna(row.Latitude) and pd.notna(row.Longitude):
            folium.Marker([row.Latitude, row.Longitude], popup=folium.Popup(
                f"<b>Name:</b><br>{row.Name}<br><b>Address:</b><br>{row.Address}, {row.City}", max_width=450)
            ).add_to(marker_cluster)
    st.subheader(f'Public Companies Reporting {metric}')
    st.components.v1.html(folium.Figure().add_child(metric_reporting_counts_map).render(), height=500)

    # add context
    metric_reporting_counts_scatterplot_context = f"There are **{reporting_metric}** public companies reporting {metric} in {states.lookup(state).name}."
    st.markdown(metric_reporting_counts_scatterplot_context)

else:
    # aggregate metric totals by state
    metric_state_totals = metric_data.groupby("State")[metric].sum().reset_index()

    # create a heatmap of companies reporting 'metric'
    geojson = "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"
    metric_state_totals_choropleth = folium.Map([43, -100], zoom_start = 4, min_zoom = 4)
    folium.Choropleth(
        geo_data=geojson,
        data=metric_state_totals,
        columns=["State", metric],
        nan_fill_opacity=0,
        line_weight = 0.25,
        key_on="feature.id",
        legend_name=f"{metric} by State",
    ).add_to(metric_state_totals_choropleth)

    st.subheader(f"{metric} by State")
    st.components.v1.html(folium.Figure().add_child(metric_state_totals_choropleth).render(), height=500)
    
    # add context
    top_metric_state_totals = metric_state_totals.nlargest(3, metric)
    top_metric_state_total1 = states.lookup(top_metric_state_totals.iloc[0]['State']).name
    top_metric_state_total2 = states.lookup(top_metric_state_totals.iloc[1]['State']).name
    top_metric_state_total3 = states.lookup(top_metric_state_totals.iloc[2]['State']).name

    bottom_metric_state_totals = metric_state_totals.nsmallest(3, metric)
    bottom_metric_state_total1 = states.lookup(bottom_metric_state_totals.iloc[0]['State']).name
    bottom_metric_state_total2 = states.lookup(bottom_metric_state_totals.iloc[1]['State']).name
    bottom_metric_state_total3 = states.lookup(bottom_metric_state_totals.iloc[2]['State']).name
    
    metric_state_totals_context = f"**{top_metric_state_total1}**, **{top_metric_state_total2}**, and **{top_metric_state_total3}** were the three states with the **greatest** {metric}, while **{bottom_metric_state_total1}**, **{bottom_metric_state_total2}**, and **{bottom_metric_state_total3}** were the three states with the **smallest** {metric}."
    st.markdown(metric_state_totals_context)

# add logo to sidebar
TUPLogo = read_logos("pictures")
st.sidebar.image(TUPLogo) 
