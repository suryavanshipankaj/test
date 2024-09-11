import streamlit as st
import pandas as pd

# Allow the user to input a custom title
dashboard_title = st.text_input("Enter the dashboard title", "HR Dashboard")

# Load data from KNIME exported files
data = pd.read_csv('knime_output.csv')

# Streamlit dashboard
st.title(dashboard_title)  # Use the user-defined title
st.write('Employee Salary Prediction')

# Display data
st.dataframe(data)

# Add more interactive user inputs (example: filter data by experience)
min_experience = st.slider('Minimum Experience (years)', min_value=int(data['Experience'].min()), max_value=int(data['Experience'].max()), value=int(data['Experience'].min()))

# Filter data based on user input
filtered_data = data[data['Experience'] >= min_experience]

# Display filtered data and chart
st.write(f"Filtered Data for Employees with at least {min_experience} years of experience:")
st.dataframe(filtered_data)

# Add charts/plots as needed
st.line_chart(filtered_data[['Experience', 'Predicted Salary']])
