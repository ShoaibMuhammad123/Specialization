import streamlit as st
import pandas as pd


st.title('Streamlit Text Input')

## To Take text input

name = st.text_input("Enter your name: ")
if name:
    st.write(f"Hellow: {name}")



## To add a slidder for Age
Age = st.slider('Select you Age: ',0,100,25)
st.write('Your Age is: ',Age)

## For a Select Box 
options = ["Matric","FSC","BS",'MS','PHD']
choice = st.selectbox("Choose your Education Level:",options)
st.write(f"Your Edcuation is: {choice}")

## Upload button for any file
upload_file = st.file_uploader("Choose a Csv file",type='csv')

if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)