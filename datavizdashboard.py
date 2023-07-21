import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
        else:
            data=pd.read_excel(uploaded_file)
            
if __name__ == "__main__":
    main()