import streamlit as st
import pandas as pd

st.title("Health and Sleep Relationship")

uploaded_file = st.file_uploader("Upload the Sleep Health and Lifestyle Dataset", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe(include='all'))

    st.subheader("Filter Data")
    filter_column = st.selectbox("Select a column to filter by", df.columns.tolist())
    unique_values = df[filter_column].dropna().unique()
    selected_value = st.selectbox("Select a value", unique_values)
    filtered_df = df[df[filter_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if numeric_columns:
        x_axis = st.selectbox("X-axis column", numeric_columns, key="x")
        y_axis = st.selectbox("Y-axis column", numeric_columns, key="y")

        if st.button("Generate Plot"):
            st.line_chart(filtered_df[[x_axis, y_axis]].set_index(x_axis))
    else:
        st.write("No numeric columns available for plotting.")

else:
    st.info("Please upload a CSV file to continue.")
