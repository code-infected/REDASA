# COVID-19 Data Analysis Platform

## Overview

This project is a COVID-19 Data Analysis Platform built using **Streamlit**, **Pandas**, and **Matplotlib**. It leverages the **REDASA COVID-19 Open Data** hosted on AWS S3, provided by the REDASA Consortium, Imperial College London. The platform allows users to load, analyze, and visualize large-scale COVID-19-related medical data to uncover insights that support ongoing research.

## Features

- **S3 Data Integration**: Seamlessly load datasets from REDASA's publicly available S3 buckets.
- **Data Preview**: View a sample of the dataset before performing any analysis.
- **Data Visualization**: Create simple plots such as line graphs to visualize trends in the dataset.
- **Real-Time Interaction**: Select different S3 buckets and files, and visualize the results on the fly.
- **Scalable Analysis**: Handle large datasets efficiently with Pandas and Matplotlib for fast and flexible analysis.

## Datasets

The platform fetches data from the following publicly accessible S3 buckets:

1. **Raw Curation Data** (`pansurg-curation-raw-open-data`)
   - A collection of medical documents in text format extracted from the CORD-19 dataset and other sources relevant to the REDASA project.
2. **Kendra Query Results** (`pansurg-curation-workflo-kendraqueryresults50d0eb-open-data`)
   - Documents surfaced by Amazon Kendra as relevant to specific medical research questions.
3. **Final Curations** (`pansurg-curation-final-curations-open-data`)
   - GroundTruth annotations created by the REDASA curator community for medical research questions.

For more information about REDASA data and its usage, refer to the [AWS Marketplace Listing](https://aws.amazon.com/marketplace/pp/prodview-zpajhdz2eccoo?sr=0-6&ref_=beagle&applicationId=AWSMPContessa#usage).

## Setup and Installation

### Prerequisites

- Python 3.7 or above
- Access to the internet for fetching data from S3 buckets

### Step 1: Clone the Repository

```bash
git clone https://github.com/code-infected/covid19-data-analysis-platform.git
cd covid19-data-analysis-platform
```

### Step 2: Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies:

```bash
# For Linux/MacOS
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit Application

Run the app using Streamlit:

```bash
streamlit run covid_analysis_app.py
```

This will launch the Streamlit app in your default web browser. You can then interact with the platform to load and visualize data from the S3 buckets.

## Application Flow

1. **Select S3 Bucket**: Choose from one of the available S3 buckets (Raw Data, Kendra Results, or Final Curations).
2. **Select File**: After selecting the bucket, choose a specific file from the bucket to load.
3. **Data Preview**: View the first few rows of the selected dataset to understand its structure.
4. **Visualize Data**: Generate a simple line plot using Matplotlib to visualize the dataset.

## Example Screenshots

### Data Preview
![Data Preview](screenshots/data-preview.png)

### Visualization Example
![Visualization Example](screenshots/visualization-example.png)

## Future Improvements

- **Advanced Visualizations**: Implement more complex visualizations like bar plots, scatter plots, and heatmaps using Seaborn or Plotly.
- **Filtering Options**: Add filtering options to allow users to explore the dataset based on specific medical conditions, time frames, or locations.
- **Statistical Analysis**: Provide basic statistics, like mean, median, or variance, on the selected datasets.
- **Download Functionality**: Enable users to download the filtered or visualized data for further analysis.

## License

This project is licensed under the [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) license.

## How to Cite

REDASA COVID-19 Open Data was accessed from [https://registry.opendata.aws/redasa-covid-data](https://registry.opendata.aws/redasa-covid-data).