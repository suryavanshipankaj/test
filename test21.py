import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Real-Time Interactive Dashboard with Streamlit")

# Upload the CSV or Excel file
uploaded_file = st.file_uploader("Upload your data (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file:
    # Load the data based on file type
    if uploaded_file.name.endswith('.csv'):
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_excel(uploaded_file)

    # Display the data
    st.write("### Data Preview")
    st.dataframe(data)

    # Allow users to select columns for visualization
    x_axis = st.selectbox("Select X-axis", data.columns)
    y_axis = st.selectbox("Select Y-axis", data.columns)

    # Create a dynamic plot
    if x_axis and y_axis:
        st.write(f"### Plot of {y_axis} vs {x_axis}")
        fig, ax = plt.subplots()
        ax.scatter(data[x_axis], data[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        st.pyplot(fig)

    # Add additional analysis, filters, or widgets for real-time interactivity
    st.write("### Summary Statistics")
    st.write(data.describe())

    # You can add more interactive elements such as sliders, checkboxes, or text input for filtering data
# Example of adding filters for user interactivity
st.write("### Filter the Data")
filter_value = st.slider("Filter by a numerical column", min_value=int(data[y_axis].min()), max_value=int(data[y_axis].max()), value=int(data[y_axis].min()))

# Filter the data based on the selected value
filtered_data = data[data[y_axis] >= filter_value]
st.write(f"Data where {y_axis} is greater than or equal to {filter_value}")
st.dataframe(filtered_data)
