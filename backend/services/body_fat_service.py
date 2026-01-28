from utils.rule_loader import load_rule

def classify_body_fat(body_fat: float, gender: str):
    ranges = body_fat_rules["categories"][gender.lower()]

    for r in ranges:
        if "min" in r and "max" in r:
            if r["min"] <= body_fat < r["max"]:
                return r["label"]
        elif "max" in r:
            if body_fat < r["max"]:
                return r["label"]
        else:
            return r["label"]

    return "Unknown"

body_fat_rules = load_rule("body_fat.json")

def calculate_body_fat(bmi: float, age: int, gender: str):
    params = body_fat_rules["parameters"]
    sex_map = body_fat_rules["sex_mapping"]

    sex_value = sex_map[gender.lower()]

    body_fat = (
        params["bmi_multiplier"] * bmi +
        params["age_multiplier"] * age -
        params["sex_multiplier"] * sex_value -
        params["constant"]
    )

    category = classify_body_fat(body_fat, gender)

    return round(body_fat, 2), category
