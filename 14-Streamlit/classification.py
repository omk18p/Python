import streamlit as st                         # Import Streamlit for building the web app
import pandas as pd                            # Import Pandas for data manipulation
from sklearn.datasets import load_iris         # Import the Iris dataset
from sklearn.ensemble import RandomForestClassifier  # Import the Random Forest classifier

# ----------------------------------------------------
# Cache the dataset so it is loaded only once
# Improves performance by avoiding repeated loading
# ----------------------------------------------------
@st.cache_data
def load_data():
    iris = load_iris()  # Load the Iris dataset

    # Convert dataset into a Pandas DataFrame
    df = pd.DataFrame(iris.data, columns=iris.feature_names)

    # Add the target (species) column
    df['species'] = iris.target

    # Return the DataFrame and species names
    return df, iris.target_names


# Load the dataset
df, target_names = load_data()

# ----------------------------------------------------
# Train the Machine Learning model
# ----------------------------------------------------

# Create a Random Forest Classifier
model = RandomForestClassifier()

# Train the model
# Features -> First four columns
# Target   -> Species column
model.fit(df.iloc[:, :-1], df['species'])

# ----------------------------------------------------
# Sidebar Inputs
# ----------------------------------------------------

# Create a title in the sidebar
st.sidebar.title("Input Features")

# Create sliders for the four flower features
sepal_length = st.sidebar.slider(
    "Sepal length",
    float(df['sepal length (cm)'].min()),
    float(df['sepal length (cm)'].max())
)

sepal_width = st.sidebar.slider(
    "Sepal width",
    float(df['sepal width (cm)'].min()),
    float(df['sepal width (cm)'].max())
)

petal_length = st.sidebar.slider(
    "Petal length",
    float(df['petal length (cm)'].min()),
    float(df['petal length (cm)'].max())
)

petal_width = st.sidebar.slider(
    "Petal width",
    float(df['petal width (cm)'].min()),
    float(df['petal width (cm)'].max())
)

# ----------------------------------------------------
# Prepare the user input for prediction
# ----------------------------------------------------

# Create a list containing the input features
input_data = [[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]]

# ----------------------------------------------------
# Make Prediction
# ----------------------------------------------------

# Predict the species (returns class index)
prediction = model.predict(input_data)

# Convert the predicted class index to the species name
predicted_species = target_names[prediction[0]]

# ----------------------------------------------------
# Display Prediction
# ----------------------------------------------------

st.write("### Prediction")

# Display the predicted flower species
st.write(f"The predicted species is: **{predicted_species}**")