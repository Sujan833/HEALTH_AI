import streamlit as st
from disease_prediction import predict_disease
from treatment_plan import generate_treatment_plan
from health_analytics import analyze_vitals
from chatbot import ask_medical_question
import pandas as pd
import matplotlib.pyplot as plt
import io
import os
st.set_page_config(page_title="HealthAI - Personal Healthcare Assistant", layout="centered", page_icon="🩺")
# Sidebar with logo
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/medical-doctor.png", width=60)
    st.header("🔍 Navigation")
    page = st.radio("Select a Page", ["Disease Prediction", "Treatment Plan", "Health Analytics", "Patient Chat"], key="page_selector")

st.title("🩺 HealthAI - Personal Healthcare Assistant")

# Initialize session state variables if not already
if "symptoms" not in st.session_state:
    st.session_state.symptoms = ""
    st.session_state.age = ""
    st.session_state.gender = ""
    st.session_state.history = ""
    st.session_state.prediction_result = None
    st.session_state.prediction_next_steps = None
    st.session_state.prediction_treatment = None
    st.session_state.condition = ""
    st.session_state.treatment_plan = None
    st.session_state.chat_question = ""
    st.session_state.chat_answer = None

if page == "Disease Prediction":
    st.subheader("🧪 Disease Prediction")
    symptoms_input = st.text_input("Enter symptoms separated by commas (e.g., fever, cough, headache)", st.session_state.symptoms)
    age_input = st.text_input("Age", st.session_state.age)
    gender_input = st.text_input("Gender", st.session_state.gender)
    history_input = st.text_input("Medical History", st.session_state.history)

    if st.button("Predict"):
        symptom_list = [s.strip() for s in symptoms_input.split(',') if s.strip()]
        profile = {"age": age_input, "gender": gender_input, "history": history_input}
        try:
            result = predict_disease(symptom_list)
            # Fallback if prediction is suspiciously generic or unknown
            if result.lower() in ["(vertigo) paroymsal positional vertigo", "unknown", "", None]:
                result = ask_medical_question(
                    f"Symptoms: {symptom_list}. Patient profile: {profile}. What disease is most likely?")

            next_steps = ask_medical_question(f"Patient profile: {profile}. Symptoms: {symptom_list}. What condition is most likely and what steps should be taken next?")
            treatment_plan = generate_treatment_plan(result, profile)

            st.session_state.symptoms = symptoms_input
            st.session_state.age = age_input
            st.session_state.gender = gender_input
            st.session_state.history = history_input
            st.session_state.prediction_result = result.strip().rstrip('. ,\n') + "."
            st.session_state.prediction_next_steps = next_steps.strip().rstrip('. ,\n') + "."
            st.session_state.prediction_treatment = treatment_plan.strip().rstrip('. ,\n') + "."
        except Exception as e:
            st.error(f"Error: {str(e)}")

    if st.session_state.prediction_result:
        st.success(f"Predicted Disease: {st.session_state.prediction_result}")
        st.info(f"Next Steps: {st.session_state.prediction_next_steps}")
        st.write("### Suggested Treatment Plan")
        st.write(st.session_state.prediction_treatment)

elif page == "Treatment Plan":
    st.subheader("💊 Treatment Plan Generator")
    st.session_state.condition = st.text_input("Condition", st.session_state.condition)
    st.session_state.age = st.text_input("Age", st.session_state.age)
    st.session_state.gender = st.text_input("Gender", st.session_state.gender)
    st.session_state.history = st.text_input("Medical History", st.session_state.history)

    if st.button("Generate Treatment Plan"):
        profile = {"age": st.session_state.age, "gender": st.session_state.gender, "history": st.session_state.history}
        try:
            result = generate_treatment_plan(st.session_state.condition, profile)
            st.session_state.treatment_plan = result.strip().rstrip('. ,\n') + "."
        except Exception as e:
            st.error(f"Error: {str(e)}")

    if st.session_state.treatment_plan:
        st.success(st.session_state.treatment_plan)

elif page == "Health Analytics":
    st.subheader("📊 Health Analytics Dashboard")
    st.write("Upload your health data (CSV)")

    uploaded_file = st.file_uploader("Upload Vitals CSV", type=["csv"])

    if uploaded_file is not None:
        temp_file_path = os.path.join("uploads", uploaded_file.name)
        if not os.path.exists("uploads"):
            os.makedirs("uploads")
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        try:
            insights = analyze_vitals(temp_file_path)
            st.success("Vitals analyzed successfully.")
            st.info(insights)
            st.image("static/vitals_plot.png")
        except Exception as e:
            st.error(f"Error: {str(e)}")

elif page == "Patient Chat":
    st.subheader("💬 Ask a Health Question")
    st.session_state.chat_question = st.text_input("Your medical question", st.session_state.chat_question)
    if st.button("Ask"):
        try:
            response = ask_medical_question(st.session_state.chat_question)
            st.session_state.chat_answer = response.strip().rstrip('. ,\n') + "."
        except Exception as e:
            st.error(f"Error: {str(e)}")

    if st.session_state.chat_answer:
        st.success(st.session_state.chat_answer)

# Add some basic branding and style at the bottom
st.markdown("""
---
<center>
<img src="https://img.icons8.com/fluency/96/medical-doctor.png" width="50" />
<b>HealthAI</b> &copy; 2025. Powered by IBM Granite Model.<br>
<small style='color:gray;'>Developed by Akula Sujan</small>
</center>
""", unsafe_allow_html=True)
