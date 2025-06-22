
# 🏥 HealthAI: Intelligent Disease Prediction System

A Flask + Streamlit based AI application that predicts diseases based on symptoms, generates treatment plans, and responds to medical queries using both ML and IBM Watson Granite models.

---

## 🚀 Features
- Disease prediction using a Naive Bayes ML model
- GenAI fallback using IBM Watson Granite for low-confidence predictions
- Symptom-based diagnosis with profile data (age, gender, history)
- Personalized treatment plan and recommendations
- Streamlit web UI + Flask backend
- IBM Cloud Foundation Model integration

---

## 📁 Folder Structure
```
HealthAI/
│
├── app.py                  # Flask backend
├── requirements.txt        # Required Python packages
├── .env                    # IBM Watson API credentials (excluded in .gitignore)
|── treatment_plan.py       # generates treatment plans
├── chatbot.py
├── disease_prediction.py   # ML logic for Naive Bayes
├── health_analytics.py     # IBM Granite fallback handling
└── venv/                   # Virtual environment (excluded in .gitignore)
```

---

## 🔧 Prerequisites
- Python 3.9 or newer
- Git installed
- IBM Cloud account (Watson Machine Learning enabled)

---

## 🛠️ Step-by-Step Setup

### 1. Clone the repository
```bash
git clone https://github.com/Sujan833/HealthAI.git
cd HealthAI
```

### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your `.env` file
Create a `.env` file in the root folder and add the following:
```
WML_URL=your_IBM_cloud_wml_url
WML_APIKEY=your_IBM_api_key
PROJECT_ID=your_IBM_project_id
GEN_MODEL_ID=granite-13b-chat
```

📝 **Note:** Never share this `.env` file publicly.

### 5. Run the Flask backend (API service)
```bash
python app.py
```

The Flask API will start at `http://localhost:5000`.

### 6. Run the Streamlit frontend
```bash
streamlit run app.py
```

Streamlit will open a browser window showing the app.

---

## ⚠️ Git Tips

### Avoid pushing large files or virtual environments:
Ensure your `.gitignore` contains:
```
venv/
__pycache__/
*.pyc
*.pkl
uploads/*
*.h5
.env
```

---

## 📦 Deployment
For cloud deployment (e.g., Heroku, Render, AWS), make sure:
- Flask app is wrapped with `gunicorn`
- Environment variables are properly set
- `Procfile` is added for Flask or Streamlit mode

---

## 💬 Questions or Help?
If you face any issues, feel free to open an issue in the repository or contact me on GitHub.
