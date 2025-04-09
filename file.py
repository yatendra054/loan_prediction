import streamlit as st
import pandas as pd
import numpy as np
import joblib


model = joblib.load('model.pkl') 


st.title('Loan Approval Prediction')


col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox('Gender', ['Male', 'Female'])
    married = st.selectbox('Marital Status', ['Yes', 'No'])
    dependents = st.selectbox('Dependents', ['0', '1', '2', '3+'])
    education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
    self_employed = st.selectbox('Self Employed', ['Yes', 'No'])

with col2:
    applicant_income = st.number_input('Applicant Income (USD)', min_value=0)
    coapplicant_income = st.number_input('Coapplicant Income (USD)', min_value=0)
    loan_amount = st.number_input('Loan Amount (USD)', min_value=0)
    loan_term = st.number_input('Loan Term (days)', min_value=0)
    credit_history = st.selectbox('Credit History', ['Yes', 'No'])
    property_area = st.selectbox('Property Area', ['Urban', 'Semiurban', 'Rural'])


def preprocess_inputs():
    
    processed = {
        'Gender': 1 if gender == 'Male' else 0,
        'Married': 1 if married == 'Yes' else 0,
        'Dependents': 0 if dependents == '0' else 1,
        'Education': 1 if education == 'Graduate' else 0,
        'Self_Employed': 1 if self_employed == 'Yes' else 0,
        'ApplicantIncome': np.log(applicant_income + 1),  
        'CoapplicantIncome': np.log(coapplicant_income + 1),
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_term,
        'Credit_History': 1 if credit_history == 'Yes' else 0,
        'Property_Area': 1 if property_area in ['Urban', 'Semiurban'] else 0
    }
    return pd.DataFrame([processed])


if st.button('Predict Loan Approval'):
    input_df = preprocess_inputs()
    prediction = model.predict(input_df)
    
    if prediction[0] == 1:
        st.success('Loan Status: Approved (Y)')
    else:
        st.error('Loan Status: Not Approved (N)')

    st.subheader('Processed Input Features')
    st.dataframe(input_df)