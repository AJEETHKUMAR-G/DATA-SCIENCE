import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Loan Prediction App",
    layout="centered"
)

@st.cache_resource
def load_artifacts():
    model = joblib.load("model_files/best_model.pkl")
    preprocessor = joblib.load("model_files/preprocessor.pkl")
    return model, preprocessor

model, preprocessor = load_artifacts()

st.title("🏦 Loan Approval Prediction")
st.markdown("Predict the **probability of loan approval** using ML")

st.divider()

with st.form("loan_form"):
    st.subheader("📋 Applicant Details")

    person_age = st.number_input("Age", 18, 100, 30)
    person_income = st.number_input("Annual Income", 10_000, 10_000_000, 500_000)
    person_emp_length = st.number_input("Employment Length (years)", 0.0, 40.0, 5.0)

    loan_amnt = st.number_input("Loan Amount", 1_000, 5_000_000, 200_000)
    loan_int_rate = st.number_input("Interest Rate (%)", 1.0, 40.0, 10.0)
    loan_percent_income = st.slider("Loan % of Income", 0.0, 1.0, 0.2)

    cb_person_cred_hist_length = st.number_input(
        "Credit History Length (years)", 0, 40, 5
    )

    cb_person_default_on_file = st.selectbox(
        "Previous Default?", ["N", "Y"]
    )

    person_home_ownership = st.selectbox(
        "Home Ownership",
        ["RENT", "OWN", "MORTGAGE", "OTHER"]
    )

    loan_intent = st.selectbox(
        "Loan Intent",
        ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"]
    )

    loan_grade = st.selectbox(
        "Loan Grade",
        ["A", "B", "C", "D", "E", "F", "G"]
    )

    submitted = st.form_submit_button("🔍 Predict")

if submitted:
    input_df = pd.DataFrame([{
        "person_age": person_age,
        "person_income": person_income,
        "person_emp_length": person_emp_length,
        "loan_amnt": loan_amnt,
        "loan_int_rate": loan_int_rate,
        "loan_percent_income": loan_percent_income,
        "cb_person_cred_hist_length": cb_person_cred_hist_length,
        "cb_person_default_on_file": cb_person_default_on_file,
        "person_home_ownership": person_home_ownership,
        "loan_intent": loan_intent,
        "loan_grade": loan_grade
    }])

    X_processed = preprocessor.transform(input_df)
    prob = model.predict_proba(X_processed)[0][1]

    st.divider()
    st.subheader("📊 Prediction Result")

    st.metric("Approval Probability", f"{prob:.2%}")

    if prob >= 0.5:
        st.success("✅ Loan Likely to be Approved")
    else:
        st.error("❌ Loan Likely to be Rejected")

    st.progress(int(prob * 100))
