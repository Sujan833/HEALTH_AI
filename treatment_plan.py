from chatbot import model  # reuse the same Granite model

def generate_treatment_plan(condition: str, profile: dict):
    prompt = (
        f"Patient condition: {condition}. Profile: {profile}. "
        "Provide a comprehensive treatment plan including medications, lifestyle changes, and tests."
    )
    return model.generate_text(prompt)
