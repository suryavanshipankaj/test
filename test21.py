import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import mysql.connector

# Database connection details
db_username = 'root'
db_password = '99999??'
db_host = 'localhost'
db_port = '3506'
db_name = 'source'

# Create a Streamlit form
st.title('User Information Form')

# Form inputs
with st.form(key='user_form'):
    username = st.text_input('Username')
    email = st.text_input('Email')
    age = st.number_input('Age', min_value=0)
    submit_button = st.form_submit_button(label='Submit')

# Save form data to CSV
if submit_button:
    # Create a DataFrame from the input data
    user_data = pd.DataFrame({
        'Username': [username],
        'Email': [email],
        'Age': [age]
    })
    
    # Save the DataFrame to a CSV file
    user_data.to_csv('user_data.csv', index=False)
    st.success('Form data saved to CSV file.')

# Upload CSV data to the database
if st.button('Upload to Database'):
    try:
        # Create a SQLAlchemy engine
        engine = create_engine(f'mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')
        
        # Read the CSV file
        user_data = pd.read_csv('user_data.csv')
        
        # Upload the data to the database
        user_data.to_sql('users', engine, if_exists='append', index=False)
        st.success('CSV data uploaded to the database.')
    except Exception as e:
        st.error(f"An error occurred: {e}")
        print(e)  # Print error details for debugging
