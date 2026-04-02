import streamlit as st
import numpy as np
import pickle

w = pickle.load(open("w_batch.pkl","rb"))
b = pickle.load(open("b_batch.pkl","rb"))
sx = pickle.load(open("sx.pkl","rb"))
sy = pickle.load(open("sy.pkl","rb"))


st.title("🏠 Bangalore House Price Prediction")
area = st.number_input(
    "Enter Area (sq ft)",
    min_value=500.0,
    step=0.1,
    format="%.2f"
)
bedrooms = int(st.number_input("Enter Bedrooms", min_value=1, step=1))

if st.button("Predict Price"):
    
    scaled = sx.transform([[area, bedrooms]])[0]
    
    scaled_price = np.dot(scaled, w) + b
    price = sy.inverse_transform([[scaled_price]])[0][0]
    
    price = max(0, price)
    st.success(f"Estimated Price: ₹ {price:.2f} Lakhs")