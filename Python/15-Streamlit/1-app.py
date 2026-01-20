import streamlit as st
import pandas as pd
import numpy as np


## Title of the application 
st.title('First Application')

## Display a simple text
st.write("This is a simple text")

## Create a simple DataFrame

df = pd.DataFrame({
    'first_col':[1,2,3,4,5],
    'second_col':[10,20,30,40,50]
})

## Display the DataFrame
st.write('Here is the dataFrame')
st.write(df)

## To Create a Line Chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)

st.line_chart(chart_data)