import streamlit as st      # Import Streamlit for building web applications
import pandas as pd         # Import Pandas for data manipulation

# -----------------------------
# Display the title of the app
# -----------------------------
st.title("Streamlit Text Input")

# Create a text input box for the user
name = st.text_input("Enter your name:")

# Create a slider to select age
# Parameters: (label, min_value, max_value, default_value)
age = st.slider("Select your age:", 0, 100, 25)

# Display the selected age
st.write(f"Your age is {age}.")

# -----------------------------
# Create a dropdown (select box)
# -----------------------------
options = ["Python", "Java", "C++", "JavaScript"]

# Display a dropdown and store the selected option
choice = st.selectbox("Choose your favorite language:", options)

# Display the selected language
st.write(f"You selected {choice}.")

# Display greeting only if the user entered a name
if name:
    st.write(f"Hello, {name}")

# -----------------------------
# Create a sample DataFrame
# -----------------------------
data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

# Convert dictionary to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
df.to_csv("sampledata.csv")

# Display the DataFrame
st.write(df)

# -----------------------------
# Upload and display a CSV file
# -----------------------------

# Create a file uploader that accepts only CSV files
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Check if the user uploaded a file
if uploaded_file is not None:

    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the uploaded DataFrame
    st.write(df)