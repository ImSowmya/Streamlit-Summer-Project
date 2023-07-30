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
        st.sidebar.title("Data Visualization")
        i = st.sidebar.selectbox("Select a column to visualize",list(data.columns),index=0)
        plt.figure()
        if data[i].dtype == np.number:
            #For numerical columns
            plot=st.sidebar.selectbox("Select the chart type ",["Histogram",'Line Chart',"Scatter Plot"])
            if plot=="Histogram":
                fig = px.histogram(data, x=i, title=f"Histogram of {i}")
            elif plot == "Line Chart":
                fig = px.line(data, x=i, y=i, title=f"Line Chart of {i}")
            elif plot == "Scatter Plot":
                fig = px.scatter(data, x=i, y=i, title=f"Scatter Plot of {i}")
        else:
            #For categorical columns
            plot=st.sidebar.selectbox("Select the chart type ",["Bar Chart","Pie Chart"])
            if plot=="Bar Chart":
                fig=px.bar(data,x=i,title=f"Bar Chart of {i}")
            if plot=="Pie Chart":
                fig=px.pie(data,names=i,title=f"Pie Chart of {i}")
        st.plotly_chart(fig)
        
        #Data Filtering
        st.header("Data Filtering")
        st.subheader("Preview of Data")
        st.dataframe(data.head())
        #Based on columns:
        st.sidebar.title("Data Filtering")
        i=st.sidebar.selectbox("Select a column to Filter",list(data.columns))
        st.subheader("Filtered Data by Column")
        if data[i].dtype==np.number:
            st.dataframe(data[i])
            min_val = st.sidebar.number_input("Minimum value", value=data[i].min())
            max_val = st.sidebar.number_input("Maximum value", value=data[i].max())
            filtered_data = data[(data[i] >= min_val) & (data[i] <= max_val)]
            st.subheader("Filtered Data by Numerical Range")
            st.dataframe(filtered_data)
        else:
            st.write(data[i])
            val=st.sidebar.multiselect("Select values to Filter ",list(data[i].unique()))
            filtered_data=data[data[i].isin(val)]
            st.subheader("Filtered Data by Categorical values")
            st.dataframe(filtered_data)
            
        # # Data Manipulation
        # st.subheader("Data Manipulation")
        # st.sidebar.title("Data Manipulation")
        # st.subheader("Un-Modified Data")
        # st.dataframe(data.head())
        # manipulation_task = st.selectbox("Select a data manipulation task", ["Add Column", "Remove Column"])
        # if manipulation_task == "Add Column":
        #     new_column_name = st.sidebar.text_input("Enter the new column name")
        #     if st.button("Add Column"):
        #         if new_column_name not in data.columns:
        #             data[new_column_name] = 0 # You can set any default value you want
        #         else:
        #             st.warning("Column with this name already exists. Please enter a different name.")

        # if manipulation_task == "Remove Column":
        #     column_to_remove = st.selectbox("Select a column to remove", list(data.columns))
        #     if st.button("Remove Column"):
        #         data.drop(column_to_remove, axis=1, inplace=True)
        
        # st.subheader("Modified Data")
        # st.dataframe(data.head())
        
        # Data Insights and Exploration
        st.header("Data Insights and Exploration")

        # Group-by Operation
        st.subheader("Group-by Operation")
        group_by_column = st.selectbox("Select a column to perform Group-by", list(data.columns))
        group_by_result = data.groupby(group_by_column).size()
        st.write(group_by_result)

        # Pivot Table
        st.subheader("Pivot Table")
        pivot_index = st.selectbox("Select a column for Pivot Table Index", list(data.columns),index=0)
        pivot_column = st.selectbox("Select a column for Pivot Table Columns", list(data.columns),index=1)
        pivot_values = st.selectbox("Select a column for Pivot Table Values", list(data.columns),index=2)
        pivot_table_result = pd.pivot_table(data, index=pivot_index, columns=pivot_column, values=pivot_values,aggfunc=np.mean)        
        st.write(pivot_table_result)
        
        st.success("Thankyou for checking out my project.")
                   
if __name__ == "__main__":
    main()