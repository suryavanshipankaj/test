import streamlit as st
import pandas as pd

# Allow the user to input a custom title
dashboard_title = st.text_input("Enter the dashboard title", "HR Dashboard")

# File uploader for the user to upload a CSV file
uploaded_file = st.file_uploader("Upload your KNIME output CSV", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    try:
        data = pd.read_csv(uploaded_file)

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

    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")

else:
    st.info("Please upload a CSV file to see the analysis.")

