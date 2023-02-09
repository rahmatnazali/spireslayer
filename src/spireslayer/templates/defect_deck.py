from spireslayer.card import Card
from spireslayer.decks import Deck
from spireslayer.templates.defect_card import LEAP, ZAP, DEFRAGMENT, THUNDER_STRIKE, GLACIER, BLIZZARD


lightning_deck = Deck([
    Card(LEAP),
    Card(LEAP),
    Card(LEAP),
    Card(ZAP),
    Card(ZAP),
    Card(ZAP),
    Card(ZAP),
    Card(DEFRAGMENT),
    Card(DEFRAGMENT),
    Card(DEFRAGMENT),
    Card(DEFRAGMENT),
    Card(THUNDER_STRIKE),
])


frost_deck = Deck([
    Card(GLACIER),
    Card(GLACIER),
    Card(GLACIER),
    Card(DEFRAGMENT),
    Card(DEFRAGMENT),
    Card(DEFRAGMENT),
    Card(BLIZZARD),
    Card(BLIZZARD),
    Card(BLIZZARD),
    Card(BLIZZARD),
    Card(BLIZZARD),
])
