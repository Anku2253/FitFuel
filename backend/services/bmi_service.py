from utils.rule_loader import load_rule

bmi_rules = load_rule("bmi.json")

def calculate_bmi(height_cm: float, weight_kg: float) -> float:
    if height_cm <= 0:
        raise ValueError("Height must be greater than zero")

    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def classify_bmi(bmi: float) -> str:
    for r in bmi_rules["ranges"]:
        if "min" in r and "max" in r:
            if r["min"] <= bmi < r["max"]:
                return r["label"]
        elif "max" in r:
            if bmi < r["max"]:
                return r["label"]
        else:
            return r["label"]

    return "Unknown"
