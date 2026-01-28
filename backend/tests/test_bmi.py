from services.bmi_service import classify_bmi

def test_bmi_underweight():
    assert classify_bmi(17.5) == "Underweight"

def test_bmi_boundary_18_5():
    assert classify_bmi(18.5) == "Normal"

def test_bmi_obese():
    assert classify_bmi(32.0) == "Obese"
