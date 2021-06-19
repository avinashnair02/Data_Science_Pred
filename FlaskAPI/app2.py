import streamlit as st
import joblib
import pickle
import numpy as np
import pandas as pd
import sklearn
# imported the required dependicies

df=pd.read_csv('salary_data_cleaned.csv')
st.title('Data Scientist Salaary Predictor')
st.title('Covid-19')

def load_models():
    file_name = "model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model


st.markdown(
    "**All the fields  are mandatory")

st.subheader('Domain & Sector')
Industry =st.

