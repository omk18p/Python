import streamlit as st      # Import Streamlit for building web applications
import pandas as pd         # Import Pandas for working with tabular data
import numpy as np          # Import NumPy for numerical operations

# -----------------------------
# Display the title of the app
# -----------------------------
st.title("Hello Streamlit")

# Display simple text on the webpage
st.write("This is a simple text")

# -----------------------------
# Create a Pandas DataFrame
# -----------------------------
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# Display a heading and the DataFrame
st.write("Here is the DataFrame:")
st.write(df)

# -----------------------------
# Create random data for a chart
# -----------------------------
# np.random.randn(20, 3) generates 20 rows and 3 columns
# of random numbers from a standard normal distribution.
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

# Display the data as an interactive line chart
st.line_chart(chart_data)