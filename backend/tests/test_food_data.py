from utils.data_loader import load_foods

def test_food_data_integrity():
    foods = load_foods()

    assert len(foods) >= 25

    for food in foods:
        assert food["calories_per_100g"] > 0
        assert food["portion_weight_g"] > 0
        assert food["category"] in {
            "roti", "rice", "dal", "sabzi",
            "fruit", "dairy", "protein", "snack", "fat"
        }
