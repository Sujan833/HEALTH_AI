from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import ast

df = pd.read_csv("data/medical_symptoms.csv")
df["Symptoms"] = df["Symptoms"].apply(lambda lst: [s.strip() for s in ast.literal_eval(lst)])
all_symptoms = sorted({s for sublist in df["Symptoms"] for s in sublist})

# Efficient one-hot encoding
symptom_df = pd.DataFrame([[int(sym in row) for sym in all_symptoms] for row in df["Symptoms"]], columns=all_symptoms)
X = symptom_df
y = df["Disease"]

model = MultinomialNB()
model.fit(X, y)

def predict_disease(symptoms: list):
    user_input = [1 if sym in symptoms else 0 for sym in all_symptoms]
    prediction = model.predict([user_input])
    return prediction[0]
