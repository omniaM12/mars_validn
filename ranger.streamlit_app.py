
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Box plots', page_icon=':chart_with_upwards_trend:')
st.title('Descriptive&Box plots')
uploaded_file= st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    column = st.selectbox('Select a column', df.columns.tolist())
    title = st.selectbox('Select chart',('Box Plot','Bar plot'))
    if title=='Box Plot':
        fig= px.box(df, x=df.index, y=df[column])
        st.plotly_chart(fig, theme=None, use_container_width=True)
        st.title("Data columns type")
        st.write(df.dtypes)
        st.title("Missings")
        st.write(df.isna().sum())
        st.title("Descriptive summary")
        st.write(df.describe())
        
    if title=='Bar plot':
        fig= px.bar(df, x=df.index, y=df[column])
        st.plotly_chart(fig, theme=None, use_container_width=True)
    dfindex= df.select_dtypes(include=np.number)
    min_index = dfindex.idxmin()
    max_index = dfindex.idxmax()

# Get the corresponding rows from the original DataFrame
    min_row = df.loc[min_index]
    max_row = df.loc[max_index]

# Display the results in Streamlit
    st.write("Row with minimum values:")
    st.write(min_row)

    st.write("Row with maximum values:")
    st.write(max_row)
    
  
    
