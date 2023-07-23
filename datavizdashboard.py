import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import streamlit as st
import os

def main():
    st.title("Data Exploration and Visualization Dashboard")

    # File upload section
    st.sidebar.title("Upload Data")
    uploaded_file = st.sidebar.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        # Load data
        file_extension = os.path.splitext(uploaded_file.name)[1].lower()
        if file_extension == ".csv":
            data = pd.read_csv(uploaded_file)
        elif file_extension==".xlsx":
            data=pd.read_excel(uploaded_file)

        # Data Summary and Statistics
        st.header("Data Summary")
        st.write(data.head())

        st.header("Basic Statistics")
        st.write(data.describe())

        # Data Visualization
        st.header("Data Visualization")
        i = st.sidebar.selectbox("Select a column to visualize",list(data.columns),index=0)
        plt.figure()
        if data[i].dtype == np.number:
            #For numerical columns, create a histogram
            plot=st.sidebar.selectbox("Select the chart type ",["Histogram",'Line Chart',"Scatter Plot"],index=0)
            if plot=="Histogram":
                fig = px.histogram(data, x=i, title=f"Histogram of {i}")
            elif plot == "Line Chart":
                fig = px.line(data, x=i, y=i, title=f"Line Chart of {i}")
            elif plot == "Scatter Plot":
                fig = px.scatter(data, x=i, y=i, title=f"Scatter Plot of {i}")
        
        
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()