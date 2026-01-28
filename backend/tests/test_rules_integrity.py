from utils.rule_loader import load_rule

def test_bmi_rules_load():
    rules = load_rule("bmi.json")
    assert "ranges" in rules
    assert len(rules["ranges"]) > 0

def test_body_fat_rules_have_formula():
    rules = load_rule("body_fat.json")
    assert rules["formula"] == "deurenberg"
    assert "parameters" in rules
