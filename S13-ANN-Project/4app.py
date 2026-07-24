import streamlit as st
import tensorflow as tf
import pandas as pd
import pickle


# cd C:\Users\Omkar\Desktop\Python\S13-ANN-Project
# python -m streamlit run app.py
# ---------------- Load Model ----------------

model = tf.keras.models.load_model("model.h5")

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

# ---------------- Streamlit App ----------------

st.title("Employee Salary Prediction")

st.write("Enter the employee details below to predict the estimated salary.")

# ---------------- User Inputs ----------------

credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)

gender = st.selectbox("Gender", ["Female", "Male"])

age = st.slider("Age", 18, 100, 35)

tenure = st.slider("Tenure", 0, 10, 5)

balance = st.number_input("Balance", min_value=0.0, value=50000.0)

num_products = st.slider("Number of Products", 1, 4, 2)

has_cr_card = st.selectbox("Has Credit Card", [0, 1])

is_active_member = st.selectbox("Is Active Member", [0, 1])

geography = st.selectbox("Geography", ["France", "Germany", "Spain"])

# ---------------- Manual Encoding ----------------

gender = 1 if gender == "Male" else 0

geo_france = 1 if geography == "France" else 0
geo_germany = 1 if geography == "Germany" else 0
geo_spain = 1 if geography == "Spain" else 0

# ---------------- Create Input ----------------

input_data = pd.DataFrame({
    "CreditScore": [credit_score],
    "Gender": [gender],
    "Age": [age],
    "Tenure": [tenure],
    "Balance": [balance],
    "NumOfProducts": [num_products],
    "HasCrCard": [has_cr_card],
    "IsActiveMember": [is_active_member],
    "Geography_France": [geo_france],
    "Geography_Germany": [geo_germany],
    "Geography_Spain": [geo_spain]
})

# ---------------- Scale ----------------

input_scaled = scaler.transform(input_data)

# ---------------- Predict ----------------

if st.button("Predict Salary"):

    prediction = model.predict(input_scaled)

    st.success(f"Estimated Salary: ${prediction[0][0]:,.2f}")