# health_analytics.py
import matplotlib.pyplot as plt
import pandas as pd

def analyze_vitals(file_path):
    df = pd.read_csv(file_path)

    # Validate required columns
    required_cols = {"date", "heart_rate", "blood_pressure", "glucose"}
    if not required_cols.issubset(df.columns):
        return "Invalid file format. Required columns: date, heart_rate, blood_pressure, glucose."

    # Convert date if needed
    df["date"] = pd.to_datetime(df["date"])

    plt.figure(figsize=(10, 6))
    plt.plot(df["date"], df["heart_rate"], marker='o', label="Heart Rate")
    plt.plot(df["date"], df["blood_pressure"], marker='s', label="Blood Pressure")
    plt.plot(df["date"], df["glucose"], marker='^', label="Glucose")
    plt.title("Health Vitals Over Time")
    plt.xlabel("Date")
    plt.ylabel("Values")
    plt.legend()
    plt.grid(True)

    output_path = "static/vitals_plot.png"
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()  # 🚨 Make sure to close to prevent memory issues

    return "Vitals analyzed and plot saved."
