import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import datetime

def load_model():
    # Path to the model file
    # We might save it in the same directory or a 'models' subdirectory
    base_path = os.path.dirname(os.path.dirname(__file__))
    model_path = os.path.join(base_path, 'projects', 'Used-Car-Price-Prediction-Model-main', 'model.pkl')
    
    if os.path.exists(model_path):
        with open(model_path, 'rb') as f:
            return pickle.load(f)
    return None

def app():
    st.header("Used Car Price Prediction")
    st.write("""
    ### Predict the selling price of your car
    Enter the details of the car below to get an estimated selling price.
    If you leave fields unchanged, default average values will be used.
    """)

    # --- UI with Defaults ---
    
    # Defaults
    current_year = datetime.datetime.now().year
    default_year = 2019
    default_price_usd = 25000.0 
    default_kms = 30000
    
    # approx conversion: 1 Lakh INR ~= $1,190 USD (at ~84 INR/USD)
    # Factor: 1 USD = 1/1190 Lakhs
    usd_to_lakhs = 1 / 1190
    lakhs_to_usd = 1190

    col1, col2 = st.columns(2)
    
    with col1:
        year = st.number_input("Year Bought", min_value=1990, max_value=current_year, value=default_year)
        present_price_usd = st.number_input("Present Showroom Price ($)", min_value=100.0, value=default_price_usd)
        kms_driven = st.number_input("Kilometers Driven", min_value=0, value=default_kms)
        owner_count = st.selectbox("Number of Previous Owners", [0, 1, 3], index=0)

    with col2:
        fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
        seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
        transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

    # Feature Engineering Logic
    car_age = current_year - year
    
    # Currency Conversion for Model
    present_price_lakhs = present_price_usd * usd_to_lakhs

    # One-Hot Encoding Logic
    fuel_diesel = 1 if fuel_type == "Diesel" else 0
    fuel_petrol = 1 if fuel_type == "Petrol" else 0
    seller_individual = 1 if seller_type == "Individual" else 0
    transmission_manual = 1 if transmission == "Manual" else 0
    
    if st.button("Predict Price"):
        model = load_model()
        
        if model:
            # Input: [Present_Price(Lakhs), Kms, Owner, Age, Diesel, Petrol, Individual, Manual]
            input_data = np.array([[
                present_price_lakhs,
                kms_driven,
                owner_count,
                car_age,
                fuel_diesel,
                fuel_petrol,
                seller_individual,
                transmission_manual
            ]])
            
            try:
                prediction_lakhs = model.predict(input_data)[0]
                prediction_usd = prediction_lakhs * lakhs_to_usd
                
                output = round(prediction_usd, 2)
                
                if output < 0:
                    st.warning("The prediction is negative. This car likely has no resale value.")
                else:
                    st.success(f"Estimated Price: $ {output:,.2f}")
            except Exception as e:
                st.error(f"Error during prediction. Feature mismatch? {e}")
                st.info("Please retrain the model to ensure feature alignment.")
        else:
            st.warning("Model not trained yet!")
            st.info("Please place 'car data.csv' in the project folder and run the training script.")

