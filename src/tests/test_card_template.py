from spireslayer.templates.defect_card import LEAP, ZAP


def test_card_template_import():
    assert LEAP == "Leap"
    assert ZAP == "Zap"
