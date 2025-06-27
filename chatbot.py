# chatbot.py

import streamlit as st
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames

def load_model():
    url = st.secrets["WML_URL"]
    api_key = st.secrets["WML_API_KEY"]
    project_id = st.secrets["WML_PROJECT_ID"]

    if not url or not api_key or not project_id:
        raise ValueError("Missing one or more required IBM Cloud credentials in Streamlit secrets.")

    credentials = {
        "url": url,
        "apikey": api_key
    }

    model = Model(
        model_id="ibm/granite-3-3-8b-instruct",
        credentials=credentials,
        project_id=project_id,
        params={
            GenTextParamsMetaNames.MAX_NEW_TOKENS: 250,
            GenTextParamsMetaNames.TEMPERATURE: 0.5
        }
    )
    return model

model = load_model()

def ask_medical_question(question: str):
    prompt = f"Answer the following medical question clearly and empathetically: {question}"
    return model.generate_text(prompt)
