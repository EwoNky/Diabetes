import streamlit as st
import joblib

# Load model
model = joblib.load('Diabetes_Logistic.model')

# Set the title
st.title("Diabetes Prediction")

# CSS for custom colors
st.markdown(
    """
    <style>
    .purple {color: purple;}
    .cyan {color: cyan;}
    </style>
    """,
    unsafe_allow_html=True
)

# Column layout
col1, col2 = st.columns(2)

# Input fields with color labels
Pregnancies = col1.number_input(label="Enter number of pregnancies", min_value=0, max_value=17)
col1.markdown('<p class="purple">Pregnancies</p>', unsafe_allow_html=True)

Glucose = col2.number_input(label="Enter Glucose level", min_value=0, max_value=191)
col2.markdown('<p class="cyan">Glucose Level</p>', unsafe_allow_html=True)

BloodPressure = col1.number_input(label="Enter Blood pressure level", min_value=0, max_value=114)
col1.markdown('<p class="purple">Blood Pressure</p>', unsafe_allow_html=True)

SkinThickness = col2.number_input(label="Enter Skin thickness level", min_value=0, max_value=99)
col2.markdown('<p class="cyan">Skin Thickness</p>', unsafe_allow_html=True)

Insulin = col1.number_input(label="Enter insulin level", min_value=0, max_value=846)
col1.markdown('<p class="purple">Insulin</p>', unsafe_allow_html=True)

BMI = col2.number_input(label="Enter BMI Score", min_value=0, max_value=67)
col2.markdown('<p class="cyan">BMI</p>', unsafe_allow_html=True)

DiabetesPedigreeFunction = col1.number_input(label="Enter DBF Score", min_value=0.078, max_value=2.42)
col1.markdown('<p class="purple">Diabetes Pedigree Function</p>', unsafe_allow_html=True)

Age = col2.number_input(label="Enter Age", min_value=21, max_value=81)
col2.markdown('<p class="cyan">Age</p>', unsafe_allow_html=True)

# Prediction button
if st.button("Predict"):
    prediction = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    if prediction == 1:
        st.success("The model predicts the patient would have Diabetes.")
    else:
        st.warning("The model predicts the patient would not have Diabetes.")