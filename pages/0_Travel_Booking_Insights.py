import streamlit as st
import pandas as pd

# Load the CSV file
@st.cache
def load_data():
    df = pd.read_csv("travel-booking-data.csv")
    return df

booking_data = load_data()

# Sidebar for selecting dimension
dimension = st.sidebar.selectbox(
    'Select Dimension to Aggregate By',
    ('Region', 'Country')
)

# Aggregate data based on selected dimension
if dimension == 'Region':
    aggregated_data = booking_data.groupby('Region')['Booking Value'].sum()
elif dimension == 'Country':
    aggregated_data = booking_data.groupby('Country')['Booking Value'].sum()

# Display the aggregated data
st.title('Booking Data Aggregation')
st.write(f'Aggregated by: {dimension}')
st.write(aggregated_data)