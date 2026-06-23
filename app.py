import streamlit as st
import joblib
import numpy as np

model = joblib.load("house_price_model.pkl")

st.title("🏠 House Price Prediction App")

st.write("Enter house details:")

area = st.number_input("Area (sq ft)", min_value=0)
bedrooms = st.number_input("Bedrooms", min_value=0)
bathrooms = st.number_input("Bathrooms", min_value=0)

if st.button("Predict Price"):
    features = np.array([[area, bedrooms, bathrooms]])
    prediction = model.predict(features)
    st.success(f"Predicted Price: {prediction[0]:,.2f}")