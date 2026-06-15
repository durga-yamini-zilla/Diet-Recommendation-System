import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("diet_model.pkl")
le_gender = joblib.load("le_gender.pkl")
le_disease = joblib.load("le_disease.pkl")
le_food = joblib.load("le_food.pkl")
le_diet = joblib.load("le_diet.pkl")

st.set_page_config(page_title="Diet Recommendation System", page_icon="🥗")

st.title("🥗 AI-Powered Diet Recommendation System")

st.write("Enter your details to get a personalized diet recommendation.")

# User Inputs
age = st.number_input("Age", min_value=1, max_value=100, value=25)

gender = st.selectbox(
    "Gender",
    le_gender.classes_
)

height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0)

weight = st.number_input("Weight (kg)", min_value=10.0, max_value=300.0, value=70.0)

bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=24.0)

disease = st.selectbox(
    "Disease",
    le_disease.classes_
)

food_pref = st.selectbox(
    "Food Preference",
    le_food.classes_
)

calories = st.number_input(
    "Calories Intake",
    min_value=500,
    max_value=5000,
    value=2000
)

if st.button("Recommend Diet"):

    gender_encoded = le_gender.transform([gender])[0]
    disease_encoded = le_disease.transform([disease])[0]
    food_encoded = le_food.transform([food_pref])[0]

    input_data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender_encoded],
        "Height_cm": [height],
        "Weight_kg": [weight],
        "BMI": [bmi],
        "Disease": [disease_encoded],
        "Food_Preference": [food_encoded],
        "Calories_Intake": [calories]
    })

    prediction = model.predict(input_data)

    recommended_diet = le_diet.inverse_transform(prediction)[0]

    st.success(f"Recommended Diet: {recommended_diet}")