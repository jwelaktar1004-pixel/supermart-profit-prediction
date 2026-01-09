import streamlit as st
import pandas as pd
import joblib

# Load model & features
model = joblib.load("rf_profit_model.pkl")
model_features = joblib.load("model_features.pkl")

st.title("🛒 Supermart Profit Prediction")

st.write("Enter order details to predict profit")

# User inputs
sales = st.number_input("Sales Amount", min_value=0.0, value=1500.0)
discount = st.slider("Discount", 0.0, 0.5, 0.2)

category = st.selectbox("Category", ["Beverages", "Snacks", "Food Grains", "Fruits & Veggies"])
sub_category = st.selectbox("Sub Category", ["Cookies", "Chocolates", "Soft Drinks", "Eggs"])
region = st.selectbox("Region", ["North", "South", "East", "West", "Central"])

year = st.selectbox("Year", [2015, 2016, 2017, 2018])
month = st.slider("Month", 1, 12, 6)
quarter = (month - 1)//3 + 1
is_weekend = st.selectbox("Weekend?", [0, 1])

# Create input dataframe
input_data = {
    "sales": sales,
    "discount": discount,
    "year": year,
    "month": month,
    "quarter": quarter,
    "is_weekend": is_weekend,
    f"category_{category}": 1,
    f"sub_category_{sub_category}": 1,
    f"region_{region}": 1
}

input_df = pd.DataFrame([input_data])

# Align columns
input_df = input_df.reindex(columns=model_features, fill_value=0)

# Predict
if st.button("Predict Profit"):
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Predicted Profit: ₹{prediction:.2f}")

