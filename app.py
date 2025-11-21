import streamlit as st
import joblib
import pandas as pd

# Load the saved model pipeline
model = joblib.load('salary_predictor_model.joblib')

# Title
st.title("Salary Predictor")

# User inputs for features
education_level = st.selectbox("Education Level", ['Bachelor', 'Master', 'PhD'])
job_title = st.text_input("Job Title")
industry = st.text_input("Industry")
location = st.text_input("Location")
company_size = st.selectbox("Company Size", ['Small', 'Medium', 'Large'])
years_experience = st.number_input("Years of Experience", min_value=0, max_value=50, step=1)
certifications = st.number_input("Number of Certifications", min_value=0, max_value=20, step=1)
age = st.number_input("Age", min_value=18, max_value=100, step=1)
working_hours = st.number_input("Working Hours per Week", min_value=0, max_value=100, step=1)

# Predict button
if st.button("Predict Salary"):
    # Prepare input data in a DataFrame
    input_data = pd.DataFrame({
        'education_level': [education_level],
        'job_title': [job_title],
        'industry': [industry],
        'location': [location],
        'company_size': [company_size],
        'years_experience': [years_experience],
        'certifications': [certifications],
        'age': [age],
        'working_hours': [working_hours]
    })

    # Predict salary using loaded model
    predicted_salary = model.predict(input_data)[0]

    # Display prediction
    st.success(f'Predicted Salary: ₹{predicted_salary:,.2f}')
    

