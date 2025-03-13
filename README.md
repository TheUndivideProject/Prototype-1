# Sustainability and Equity Environmental Dashboard (SEED) Prototype 1

## Project Description
This dashboard aims to provide insights into philanthropic spending related to environmental causes by analyzing SEC and IRS data. The goal is to make philanthropic giving data more accessible and understandable, identify the sources of funding, and reveal where and to whom these funds are being directed. This information will be compiled into a dashboard tool to aid donors, communities, and policymakers in making informed decisions about environmental giving.

Transparency is our number one goal. Although current data is accessible via the SEC and IRS, the breadth and depth of this data makes it extremely difficult for those at large without much data science experience to analyze accountability of how philanthropic giving operates in cities of interest and whether this philanthropic giving is reported. This guts the ideal of a feedback loop between the donors that are giving, and the impacted communities that are supposed to receive assistance.

Thus, our objective is to reestablish this feedback loop between communities and philanthropic giving officers, ensuring that the perspectives and leadership of community members are at the forefront of all funding decisions.

This will start as comparative analysis of Corporations and Nonprofits. This will be done through documents provided by the Securities and Exchange Commission (SEC) and the IRS (through their Business Master File and Form 990s).

## Folder Structure
- `streamlit/`: Contains all Streamlit app components.
  - `data/`: 
    - `corporate/`:  
      - `raw/`: Original CSV files downloaded from the SEC website (see details under **About the Data**).  
      - `processed/`: Processed CSV files.  
      - `preprocessing.ipynb`: Jupyter Notebook that outlines the steps for cleaning, transforming, and preparing the raw data for visualization.  
  - `pages/`:  
    - `📊 Corporate_SEC_Dashboard.py`: Documents insights from financial and philanthropic metrics from the Securities and Exchange Commission (SEC) financial statements of public companies.  
    - `📋 Nonprofit_IRS_Dashboard.py`: Documents insights from financial and philanthropic metrics from the IRS Exempt Organizations Business Master File and Form 990 filings of tax-exempt organizations.  
  - `Home.py`: Main landing page of the Streamlit app, providing a brief introduction to SEED and the goals of each dashboard.
 
## Getting Started
1. Clone the repo.

   ```
   $ git clone https://github.com/TheUndivideProject/Prototype-1.git
   ```

2. Install the requirements.

   ```
   $ pip install -r requirements.txt
   ```
3. Run the Streamlit app.
    ```
   $ streamlit run Home.py
   ```
## About the Data  

### IRS Nonprofit Data  

**1️⃣ Exempt Organizations Business Master File (EOBMF)**  
- **What it is**: A dataset containing registered nonprofit organizations.  
- **Why it matters**: Helps identify which nonprofits are active and under what classification.  
- **More info**: [IRS EOBMF](https://www.irs.gov/charities-non-profits/exempt-organizations-business-master-file-extract-eo-bmf)

**2️⃣ Form 990 Filings**  
- **What it is**: Detailed financial reports submitted by nonprofits to the IRS.  
- **Why it matters**: Provides insights into revenue, expenses, program spending, and governance.  
- **More info**: [IRS Form 990 Overview](https://www.irs.gov/forms-pubs/about-form-990)

**3️⃣ Form 990-PF (Private Foundations)**  
- **What it is**: A version of Form 990 specifically for private foundations.  
- **Why it matters**: Shows how foundations distribute grants and manage their endowments.  
- **More info**: [IRS Form 990-PF](https://www.irs.gov/forms-pubs/about-form-990-pf)

**4️⃣ Form 990-EZ**  
- **What it is**: A simplified Form 990 for smaller nonprofits.  
- **Why it matters**: Allows analysis of smaller nonprofits that may not file full 990s.  
- **More info**: [IRS Form 990-EZ](https://www.irs.gov/forms-pubs/about-form-990-ez)

### SEC Corporate Data  

**1️⃣ Financial Statement and Notes Submission Data Set**  
- **What it is**: A dataset containing all SEC-registered companies.  
- **Why it matters**: Provides insights into active companies, their locations, and the level of detail in their financial reports.  
- **More info**: [SEC Financial Statement and Notes Data Sets](https://www.sec.gov/data-research/sec-markets-data/financial-statement-notes-data-sets)

**2️⃣ Financial Statement and Notes Numeric Data Set**  
- **What it is**: A dataset containing numeric data from SEC-registered companies' filings, including detailed figures from financial statements and notes.  
- **Why it matters**: Provides insights into revenue, environmental loss contingencies, and charitable contributions.  
- **More info**: [SEC Financial Statement and Notes Data Sets](https://www.sec.gov/data-research/sec-markets-data/financial-statement-notes-data-sets)

