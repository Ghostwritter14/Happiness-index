import streamlit as st
import plotly.express as px
import pandas as pd

# Title
st.title("The pursuit of Happiness")

# Select-boxes
option_x = st.selectbox("Select the data for the X-axis",
                       ("GDP", "Happiness", "Generosity"))
option_y = st.selectbox("Select the data for the Y-axis",
                        ("GDP", "Happiness", "Generosity"))

# Data frame
df = pd.read_csv("happy.csv")

# Matching the values
match option_x:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]

# Match value of y
match option_y:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]

# Sub-header
st.subheader(f"{option_x} and {option_y}")

# Graph
figure1 = px.scatter(x=x_array, y=y_array,
                     labels={"x": option_x,
                             "y": option_y})
st.plotly_chart(figure1)


