import streamlit as st
import numpy as np
import pandas as pd
import pickle

df = pd.read_csv('cleaned.csv')
model = pickle.load(open('model.pkl','rb'))

st.title("Welcome to Bangalore House Price Predictor")
st.markdown("Want to predict the price of a new House in Bangalore? Try filling the details below:")

location = st.selectbox("Select the Location:",sorted(df['location'].unique()))
bhk = st.selectbox("Enter BHK:",sorted(df['bhk'].unique()))
bath = st.selectbox("Enter Number of Bathrooms:",sorted(df['bath'].unique()))
total_sqft = st.selectbox("Enter Total Square Feet",sorted(df['total_sqft'].unique()))

if st.button("Predict Price"):

    result = model.predict(pd.DataFrame(np.array([location, total_sqft, bath, bhk]).reshape(1, 4),
                                          columns=['location', 'total_sqft', 'bath', 'bhk']))[0] * 100000
    res = str(np.round(result,2))
    st.header(res+"Rs")


