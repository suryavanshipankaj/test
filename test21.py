import streamlit as st
import pandas as pd

# File uploader
uploaded_file = st.file_uploader("Upload an Excel or CSV file", type=['csv', 'xlsx'])

if uploaded_file:
    # Check if it's CSV or Excel
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("### Data Preview", df.head())

    # Sidebar for analysis options
    analysis_type = st.sidebar.selectbox("Choose Analysis Type", ["Summary Statistics", "Data Visualization"])

    if analysis_type == "Summary Statistics":
        st.write("### Summary Statistics")
        st.write(df.describe())

    elif analysis_type == "Data Visualization":
        chart_type = st.sidebar.selectbox("Select Chart Type", ["Bar Chart", "Line Chart", "Scatter Plot"])
        selected_columns = st.sidebar.multiselect("Select Columns", df.columns)

        if selected_columns:
            if chart_type == "Bar Chart":
                st.bar_chart(df[selected_columns])
            elif chart_type == "Line Chart":
                st.line_chart(df[selected_columns])
            elif chart_type == "Scatter Plot" and len(selected_columns) == 2:
                st.write("### Scatter Plot")
                st.scatter_chart(df[selected_columns])
