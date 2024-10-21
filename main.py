import streamlit as st 
import pandas as pd
import matplotlib.pylab as plt

st.title("Data Display Dashboard")

uploaded_data = st.file_uploader("Choose a CSV File", type="csv")

if uploaded_data is not None:
    df = pd.read_csv(uploaded_data)
    
    st.subheader("Data Preview")
    st.write(df.head())
    
    st.subheader("Data Summary")
    st.write(df.describe())
    
    st.subheader("Filter Data")
    cols = df.columns.tolist()
    selected_cols = st.selectbox("Select column to filter by", cols)
    
    unique_vals = df[selected_cols].unique()
    selected_vals = st.selectbox("Select Value", unique_vals)
    
    filtered_df = df[df[selected_cols] == selected_vals] #filters all the unique values in the given dataframe and selects those unique rows
    
    st.write(filtered_df)
    
    st.subheader("Plot Data")
    x_col = st.selectbox("Select the X-axis column",cols)
    y_col = st.selectbox("Select the Y-axis column",cols)
    
    if st.button("Plot Data"):
        st.line_chart(filtered_df.set_index(x_col)[y_col])
    else:
        st.write("Waiting for file upload")