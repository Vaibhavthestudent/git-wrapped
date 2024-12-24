import streamlit as st

st.title("BMI Calculator")

# Input fields
weight = st.number_input("Enter your weight (kg):", min_value=0.0, step=0.1)
height = st.number_input("Enter your height (m):", min_value=0.0, step=0.01)

# Calculate BMI
if height > 0:
    bmi = weight / (height ** 2)
    st.write("Your BMI is:", round(bmi, 2))
else:
    st.write("Please enter a valid height.")
