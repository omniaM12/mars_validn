
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Range validation with plotting', page_icon=':chart_with_upwards_trend:')
st.title('Descriptive&Box plots')
uploaded_file= st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())
    column = st.selectbox('Select a column', df.columns.tolist())
    title = st.selectbox('Select chart',('Box Plot','Bar plot'))
    minr= st.number_input("Insert a min number", value=None, placeholder="Type a number...")
    st.write("The min number is ", minr)
    maxr= st.number_input("Insert a max number", value=None, placeholder="Type a number...")
    st.write("The max number ", maxr)
    st.title("Data columns type")
    st.write(df.dtypes)
    st.title("Missings")
    st.write(df.isna().sum())
    percent_missing = df.isnull().sum() * 100 / len(df)
    if any(percent_missing>30):
        st.write("At least one column has more than 30% missing values.")
        columns_with_high_missingness = percent_missing[percent_missing > 30].index.tolist()
        st.write("Columns with more than 30% missing values:", columns_with_high_missingness)
        st.write("please check the columns with missings",columns_with_high_missingness)
    else:
        st.write("No columns have more than 30% missing values.")   
    st.title("Descriptive summary")
    st.write(df.describe())
        
    if title=='Bar plot':
        fig= px.bar(df, x=df.index,y=df[column])
        st.plotly_chart(fig, theme=None, use_container_width=True)

    numeric_columns = df.select_dtypes(include=np.number)
    with st.container():
    # Define the number of columns in each row
        cols = 2

    # Iterate over numeric columns and create subplots
        for i in range(0, len(numeric_columns), cols):
             col1, col2 = st.columns(cols)

             with col1:
                fig = px.box(df, y=numeric_columns[i], title=f"Box Plot for {numeric_columns[i]}")
                st.plotly_chart(fig)

             if i + 1 < len(numeric_columns):
                with col2:
                   fig = px.box(df, y=numeric_columns[i+1], title=f"Box Plot for {numeric_columns[i+1]}")
                   st.plotly_chart(fig)


    
    #with st.container():
        #for i in numeric_columns:
            #fig = px.box(df, y=df[i], title=f"Box Plot for {i}")
            #st.plotly_chart(fig)
    if column in numeric_columns:
        if title=='Box Plot':
            fig1= px.box(df, y=column,title=f"Box Plot for {column}")
            st.plotly_chart(fig1, theme=None, use_container_width=True)        
        filtered_df_less_than_minr = df[df[column] <= minr]
        filtered_df_greater_than_maxr = df[df[column] >= maxr]
    # Display the filtered DataFrames
        if not filtered_df_less_than_minr.empty:
            st.write("Rows less than min value:")
            st.write(filtered_df_less_than_minr)

        else:
            st.write("No rows found less than min value.")

        if not filtered_df_greater_than_maxr.empty:
            st.write("Rows greater than max value:")
            st.write(filtered_df_greater_than_maxr)
        else:
            st.write("No rows found greater than max value.")
    
   

  
    
