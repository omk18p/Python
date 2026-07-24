# Import Streamlit for creating the web application.
import streamlit as st

# Import NumPy for numerical operations.
import numpy as np

# Import TensorFlow to load the trained ANN model.
import tensorflow as tf

# Import preprocessing classes used during training.
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder

# Import Pandas for data manipulation.
import pandas as pd

# Import Pickle to load saved encoders and scaler.
import pickle


# Commands to run the Streamlit application.
# cd C:\Users\Omkar\Desktop\Python\S13-ANN-Project
# python -m streamlit run 3app.py


# Load the trained ANN model.
model = tf.keras.models.load_model('model.h5')


# Load the saved LabelEncoder for Gender.
with open('label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)

# Load the saved OneHotEncoder for Geography.
with open('onehot_encoder_geo.pkl', 'rb') as file:
    onehot_encoder_geo = pickle.load(file)

# Load the saved StandardScaler.
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)


# Create the Streamlit application title.
st.title('Customer Churn Prediction')


# ---------------- User Input ----------------

# Dropdown to select customer's country.
geography = st.selectbox('Geography', onehot_encoder_geo.categories_[0])

# Dropdown to select customer's gender.
gender = st.selectbox('Gender', label_encoder_gender.classes_)

# Slider for customer's age.
age = st.slider('Age', 18, 92)

# Input for account balance.
balance = st.number_input('Balance')

# Input for customer's credit score.
credit_score = st.number_input('Credit Score')

# Input for estimated salary.
estimated_salary = st.number_input('Estimated Salary')

# Slider for account tenure.
tenure = st.slider('Tenure', 0, 10)

# Slider for number of bank products.
num_of_products = st.slider('Number of Products', 1, 4)

# Dropdown for credit card ownership.
has_cr_card = st.selectbox('Has Credit Card', [0, 1])

# Dropdown for active membership status.
is_active_member = st.selectbox('Is Active Member', [0, 1])


# ---------------- Prepare Input Data ----------------

# Create a DataFrame from the user inputs.
# Gender is label encoded before storing.
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})


# One-hot encode the Geography feature.
geo_encoded = onehot_encoder_geo.transform([[geography]]).toarray()

# Convert encoded geography into a DataFrame.
geo_encoded_df = pd.DataFrame(
    geo_encoded,
    columns=onehot_encoder_geo.get_feature_names_out(['Geography'])
)

# Concatenate encoded geography with remaining features.
input_data = pd.concat(
    [input_data.reset_index(drop=True), geo_encoded_df],
    axis=1
)


# ---------------- Scale Input ----------------

# Scale the input using the saved StandardScaler.
input_data_scaled = scaler.transform(input_data)


# ---------------- Prediction ----------------

# Predict churn probability using the trained model.
prediction = model.predict(input_data_scaled)

# Extract the probability value.
prediction_proba = prediction[0][0]

# Display the churn probability.
st.write(f'Churn Probability: {prediction_proba:.2f}')

# Display the prediction result.
if prediction_proba > 0.5:
    st.write('The customer is likely to churn.')
else:
    st.write('The customer is not likely to churn.')
