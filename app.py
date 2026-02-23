"""
Car Price Predictor Application
A Streamlit web interface that loads a pre-trained machine learning pipeline
to estimate car prices based on user inputs.
"""

import joblib
import pandas as pd
import streamlit as st

# ==========================================
# 1. LOAD MODEL
# ==========================================
# Load the pre-trained machine learning pipeline
@st.cache_resource  # Caches the model so it doesn't reload on every UI interaction
def load_model():
    return joblib.load('car_price_prediction.joblib')

pipeline_model = load_model()

# ==========================================
# 2. USER INTERFACE (UI)
# ==========================================
st.title('🚗 Car Price Predictor')
st.write('Enter the car features below to estimate its market price.')

# Input fields for car features
brand_input = st.selectbox('Car Brand', ['Toyota', 'BMW', 'Mercedes', 'Hyundai', 'Kia'])
fuel_input = st.selectbox('Fuel Type', ['Petrol', 'Diesel'])
year_input = st.slider('Manufacturing Year', min_value=2000, max_value=2026, value=2015)
engine_input = st.number_input('Engine Volume (L)', min_value=1.0, max_value=10.0, value=2.0, step=0.1)
mileage_input = st.number_input('Mileage (km)', min_value=0, max_value=500000, value=50000, step=1000)

# ==========================================
# 3. PREDICTION LOGIC
# ==========================================
if st.button('Find Price!'):
    
    # Structure the user inputs into a DataFrame that matches the model's training data
    input_data = pd.DataFrame([{
        'brand': brand_input,
        'year': year_input,
        'engine': engine_input,
        'mileage': mileage_input,
        'fuel': fuel_input
    }])

    # Predict the price using the loaded pipeline
    predicted_price = pipeline_model.predict(input_data)

    # Display the formatted result
    st.success(f'💰 The estimated price of this car is approximately **{int(predicted_price[0]):,} AZN**')