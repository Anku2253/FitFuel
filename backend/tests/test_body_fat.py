from services.body_fat_service import calculate_body_fat

def test_body_fat_male_normal():
    bf, category = calculate_body_fat(
        bmi=22.0,
        age=25,
        gender="male"
    )

    assert bf > 8
    assert bf < 20
    assert category == "Normal"
