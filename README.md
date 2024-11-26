# D2k-Assignment

# New York Taxi Trip Data Pipeline

## Project Overview

This project implements a scalable and efficient data pipeline to process and analyze New York Taxi Trip data for the year 2019. The pipeline automates data extraction, processes and transforms the data, loads it into an SQLite database, and performs in-depth analysis to derive actionable insights.

### Key Features

- Automated downloading of raw taxi trip data.
- Data cleaning and transformation to generate meaningful metrics like trip duration and average speed.
- Efficient data loading into an SQLite database for storage and querying.
- Analytical reporting and visualization of key trends, including:
  - Peak hours for taxi usage.
  - Effect of passenger count on fares.
  - Year-over-Year (YoY) taxi usage trends.

---

## Environment Setup

### Prerequisites

1. Install Python (version 3.8 or higher).
2. Clone the repository to your local machine.
3. Install required dependencies by running:

   ```bash
   python -m venv venv
   python venv\Scripts\activate
   pip install -r requirements.txt

## Project Structure

D2K_Assignment/
├── scripts/
│   ├── data_extraction.py    # Handles data downloading  

│   ├── data_processing.py    # Cleans and transforms data  

│   ├── data_load.py          # Loads data into SQLite database  

├── data/                     # Directory for raw and processed data  

├── sql/                      # Directory for SQLite database  

    ├── nyc_taxi_data.db      # sqlite3 database file          

├── visualizations/           # Directory for generated charts  

├── Analysis.ipynb            # Notebook for analysis and visualization  

├── requirements.txt          # Python dependencies  

└── README.md                 # Documentation  


## Running the Project

Using the Jupyter Notebook
The entire data pipeline, from extraction to analysis, is executed in the Analysis.ipynb Jupyter
After setup the the project:
1.open Analysis.ipynb  

2.select appropreat kernel  

3.execute all run all cell command in notebook  

[Analysis.ipynb](https://github.com/deepakdubey9887/D2K_Assignment/blob/main/Analysis.ipynb)


