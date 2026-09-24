# UPI-GROWTH-ANALYSIS

#UPI Growth in India (2021-2026) - Data Analysis Project

# Project Overview
This project analyzes the unprecedented growth of the Unified Payments Interface (UPI) system in India over a five-year period from April 2021 to March 2026. By processing historical banking data, this analysis measures total transaction volumes, monetary values, and individual bank performances to visualize the scale of digital payment adoption in India. 

## Tech Stack
* **Python (Pandas, NumPy):** Used for data extraction, initial cleaning, and formatting raw transaction data.
* **SQL:** Utilized for querying the database, filtering records, and aggregating transaction metrics by bank and date.
* **Power BI:** Built an interactive dashboard to visualize key metrics, utilizing DAX formulas for dynamic calculations.

## Key Insights & Dashboard
<img width="1372" height="742" alt="Screenshot 2026-09-24 234917" src="https://github.com/user-attachments/assets/0569a5a3-927a-4466-bff7-d481c5a021cc" />


Based on the analysis, the dashboard highlights several major milestones in India's digital payment ecosystem:
* **Massive Volume:** The UPI system processed **688.33 Billion** total transactions across the five-year period.
* **Economic Scale:** The total transaction value reached a staggering **99.81 Million Crores**.
* **Top Sender:** State Bank of India (SBI) leads the ecosystem in remitter volume (60B+ transactions), making up roughly 64% of the share volume among top senders.
* **Top Receiver:** Axis Bank holds the top position for beneficiary transaction volume.
* **Consistent Growth:** Month-over-month adoption shows a continuous, uninterrupted upward trajectory from 2021 through 2026.



## Project Files
* `data_cleaning.py` / `analysis.ipynb`: Python scripts containing the Pandas and NumPy logic used to clean the raw UPI datasets and handle missing values.
* `queries.sql`: The SQL queries used to aggregate transaction volumes and values by remitter and beneficiary banks.
* `UPI_Growth_Dashboard.pbix`: The final interactive Power BI file containing the data model, DAX measures (e.g., Total Money Transactions), and visual reports.

## How to Run
1. Clone this repository to your local machine.
2. Review the Python scripts for the data cleaning methodology.
3. The SQL file can be run against your preferred relational database management system (RDBMS) if the raw data is imported.
4. Open the `.pbix` file using Power BI Desktop to interact with the dashboard, filter by specific banks, and view the underlying DAX calculations.

## Author
**Prajwal Kaluram Abhang**
