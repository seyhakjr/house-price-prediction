# import streamlit as st
# import numpy as np
# import pandas as pd
# import joblib

# # Load the trained model
# model = joblib.load('model/model.pkl')

# # Set up the Streamlit app title
# st.title('House Price Prediction')

# # Create input fields for the user to enter house features
# st.sidebar.header('Input House Features')
# bedrooms = st.sidebar.number_input('Number of Bedrooms', min_value=1, max_value=10, value=3, step=1)
# bathrooms = st.sidebar.number_input('Number of Bathrooms', min_value=1, max_value=10, value=2, step=1)
# sqft_living = st.sidebar.number_input('Square Feet of Living Space', min_value=500, max_value=10000, value=1400, step=50)
# floors = st.sidebar.number_input('Number of Floors', min_value=1, max_value=5, value=1, step=1)
# condition = st.sidebar.slider('Condition (1: Poor, 5: Excellent)', min_value=1, max_value=5, value=3)
# sqft_above = st.sidebar.number_input('Square Feet Above Ground', min_value=500, max_value=10000, value=1400, step=50)
# street = st.sidebar.number_input('Street Number', min_value=1, max_value=1000, value=75, step=1)
# city = st.sidebar.number_input('City Code', min_value=1, max_value=100, value=14, step=1)
# statezip = st.sidebar.number_input('State/Zip Code', min_value=1, max_value=100, value=2, step=1)

# # Collect the inputs into a DataFrame
# house_features = pd.DataFrame({
#     'bedrooms': [bedrooms],
#     'bathrooms': [bathrooms],
#     'sqft_living': [sqft_living],
#     'floors': [floors],
#     'condition': [condition],
#     'sqft_above': [sqft_above],
#     'street': [street],
#     'city': [city],
#     'statezip': [statezip]
# })

# # Display the input data
# st.write('### Input House Features')
# st.write(house_features)

# # Make predictions
# if st.button('Predict Price'):
#     # Predict log-transformed price
#     prediction = model.predict(house_features)

#     # Apply exponential transformation to get the actual price
#     actual_price = np.exp(prediction[0])

#     # Display the predicted price
#     st.write(f'### Predicted House Price: ${actual_price:,.2f}')





# # Load the trained model
# model = joblib.load('model/model.pkl')

# # Custom HTML and CSS for styling
# st.markdown("""
#     <style>
#     /* General Styling */
#     body {
#         background: linear-gradient(to bottom, #74ebd5, #ACB6E5);
#         color: #333;
#         font-family: Arial, sans-serif;
#     }

#     /* Sidebar Styling */
#     .sidebar .sidebar-content {
#         background: #ffffff;
#         padding: 10px;
#         border-radius: 10px;
#         border: 2px solid #ccc;
#     }
#     .sidebar h1, .sidebar h2, .sidebar h3, .sidebar h4 {
#         color: #333;
#     }
#     .sidebar .stNumberInput input {
#         border-radius: 5px;
#         border: 1px solid #aaa;
#     }

#     /* Main Header */
#     h1 {
#         text-align: center;
#         color: #ffffff;
#         background-color: #4CAF50;
#         padding: 10px 20px;
#         border-radius: 8px;
#         font-size: 2.5rem;
#     }

#     /* Prediction Button Styling */
#     .stButton button {
#         background-color: #4CAF50;
#         color: white;
#         border: none;
#         padding: 10px 20px;
#         font-size: 16px;
#         border-radius: 5px;
#         cursor: pointer;
#         transition: 0.3s;
#     }
#     .stButton button:hover {
#         background-color: #45a049;
#     }

#     /* Prediction Result */
#     .result {
#         text-align: center;
#         background-color: #ffcccb;
#         color: #333;
#         font-size: 1.5rem;
#         padding: 20px;
#         margin-top: 20px;
#         border-radius: 8px;
#         border: 2px solid #f44336;
#     }

#     </style>
# """, unsafe_allow_html=True)

# # App Title
# st.title('🏡 House Price Prediction')

# # Sidebar Input Section
# st.sidebar.header('Input House Features')
# bedrooms = st.sidebar.number_input('Number of Bedrooms', min_value=1, max_value=10, value=3, step=1)
# bathrooms = st.sidebar.number_input('Number of Bathrooms', min_value=1, max_value=10, value=2, step=1)
# sqft_living = st.sidebar.number_input('Square Feet of Living Space', min_value=500, max_value=10000, value=1400, step=50)
# floors = st.sidebar.number_input('Number of Floors', min_value=1, max_value=5, value=1, step=1)
# condition = st.sidebar.number_input('Condition (1: Poor, 5: Excellent)', min_value=1, max_value=5, value=3, step=1)
# sqft_above = st.sidebar.number_input('Square Feet Above Ground', min_value=500, max_value=10000, value=1400, step=50)
# street = st.sidebar.number_input('Street Number', min_value=1, max_value=1000, value=75, step=1)
# city = st.sidebar.number_input('City Code', min_value=1, max_value=100, value=14, step=1)
# statezip = st.sidebar.number_input('State/Zip Code', min_value=1, max_value=100, value=2, step=1)

# # Collect Inputs into a DataFrame
# house_features = pd.DataFrame({
#     'bedrooms': [bedrooms],
#     'bathrooms': [bathrooms],
#     'sqft_living': [sqft_living],
#     'floors': [floors],
#     'condition': [condition],
#     'sqft_above': [sqft_above],
#     'street': [street],
#     'city': [city],
#     'statezip': [statezip]
# })

# # Display Input Features
# st.write('### Input House Features')
# st.write(house_features)

# # Make Predictions
# if st.button('Predict Price'):
#     # Predict log-transformed price
#     prediction = model.predict(house_features)

#     # Apply exponential transformation to get the actual price
#     actual_price = np.exp(prediction[0])

#     # Display the Prediction Result
#     st.markdown(f"<div class='result'>Predicted House Price: ${actual_price:,.2f}</div>", unsafe_allow_html=True)


import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('model/model.pkl')

# Custom HTML and CSS for Styling
st.markdown("""
    <style>
    body {
        background-color: #f9f9f9;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        max-width: 500px;
        margin: auto;
    }
    h1 {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        color: #333333;
        margin-bottom: 20px;
    }
    .stNumberInput > label {
        font-weight: bold;
    }
    .stButton button {
        background-color: #007BFF;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;
        transition: 0.3s ease;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    </style>
""", unsafe_allow_html=True)

# Title Section
st.title("🏡 HOUSE PRICE PREDICTION")

# Input Fields for House Features
st.write("### Enter the House Details")

bedrooms = st.number_input("🛏️ Number of Bedrooms:", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("🛁 Number of Bathrooms:", min_value=1, max_value=10, value=2)
sqft_living = st.number_input("📐 Living Area (sqft):", min_value=500, max_value=10000, value=1400, step=50)
floors = st.number_input("🏠 Number of Floors:", min_value=1, max_value=5, value=1)
condition = st.number_input("📊 Condition (1 = Poor, 5 = Excellent):", min_value=1, max_value=5, value=3)
sqft_above = st.number_input("📏 Square Feet Above Ground:", min_value=500, max_value=10000, value=1400, step=50)
street = st.number_input("📍 Street Number:", min_value=1, max_value=1000, value=75)
city = st.number_input("🌆 City Code:", min_value=1, max_value=100, value=14)
statezip = st.number_input("📬 State/ZIP Code:", min_value=1, max_value=100, value=2)

# Predict Button
if st.button("Predict Price"):
    # Create Input DataFrame
    house_features = pd.DataFrame({
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'sqft_living': [sqft_living],
        'floors': [floors],
        'condition': [condition],
        'sqft_above': [sqft_above],
        'street': [street],
        'city': [city],
        'statezip': [statezip]
    })
    
    # Perform Prediction
    prediction = model.predict(house_features)
    price_exp = np.exp(prediction[0])  # Apply exponential transformation
    
    # Display the Predicted Price
    st.write(f"### Predicted House Price: **${price_exp:,.2f}**")
