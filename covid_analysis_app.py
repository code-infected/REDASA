import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import subprocess

# Step 1: Function to download data from S3 bucket using AWS CLI
def download_data_from_s3():
    # Directory where data will be saved
    download_dir = './data/'
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # AWS S3 command to list and download the files
    s3_bucket = "s3://pansurg-curation-raw-open-data/cord19/AWSCORD19/upload_date=1591730933/"
    st.write("Downloading data from S3 bucket...")
    
    try:
        # List files in the S3 directory
        list_command = f"aws s3 ls --no-sign-request {s3_bucket}"
        subprocess.run(list_command, shell=True, check=True)
        
        # Download all `.txt` files
        download_command = f"aws s3 cp --no-sign-request {s3_bucket} {download_dir} --recursive --exclude '*' --include '*.txt'"
        subprocess.run(download_command, shell=True, check=True)
        st.write("Data downloaded successfully.")
    except subprocess.CalledProcessError as e:
        st.error("Error in downloading data: " + str(e))

# Step 2: Function to process text data
def load_and_process_text_data():
    text_files = [f for f in os.listdir('./data/') if f.endswith('.txt')]
    
    if not text_files:
        st.error("No text files found. Make sure data is downloaded.")
        return None
    
    # Read and combine all text files
    all_text_data = ""
    for file in text_files:
        with open(f"./data/{file}", 'r') as f:
            all_text_data += f.read() + "\n"
    
    return all_text_data

# Step 3: Function to visualize data
def visualize_data(word_count):
    # Convert word counts into a Pandas DataFrame
    df = pd.DataFrame(list(word_count.items()), columns=['Word', 'Count']).sort_values(by='Count', ascending=False).head(20)
    
    # Create bar chart
    st.write("Top 20 Most Frequent Words in the Data")
    fig, ax = plt.subplots()
    ax.bar(df['Word'], df['Count'])
    plt.xticks(rotation=90)
    st.pyplot(fig)

# Step 4: Function to perform simple text analysis (word frequency)
def perform_text_analysis(text_data):
    words = text_data.split()
    word_count = {}
    
    for word in words:
        word = word.lower()  # Convert to lowercase
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

# Step 5: Streamlit app layout and main logic
st.title('COVID-19 Data Analysis Platform')
st.write("Analyze and visualize text data from the REDASA public S3 COVID-19 dataset.")

# Option to download data
if st.button('Download Data from S3'):
    download_data_from_s3()

# Load and process data
if os.path.exists('./data/'):
    text_data = load_and_process_text_data()
    if text_data:
        st.write("Data Preview:")
        st.text(text_data[:500])  # Show first 500 characters of the text data
        
        # Perform text analysis
        word_count = perform_text_analysis(text_data)
        
        # Visualize results
        visualize_data(word_count)

st.write("© 2024 | COVID-19 Data Analysis Platform")
