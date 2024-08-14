from spireslayer.card import Card
from spireslayer.decks import Deck
from spireslayer.templates.watcher_card import *
from spireslayer.templates.colorless_card import INSIGHT, FLASH_OF_STEEL

calm_and_neutral = Deck([
    Card(INNER_PEACE),
    Card(EMPTY_MIND),
    Card(EMPTY_MIND),
    Card(FLURRY_OF_BLOWS),
    Card(FLURRY_OF_BLOWS),
    Card(FLURRY_OF_BLOWS)
])

calm_and_wrath = Deck([
    Card(RUSHDOWN),
    Card(ERUPTION),
    Card(INDIGNATION)
])

divinity_and_wrath = Deck([
    Card(PRAY),
    Card(PROSTRATE),
    Card(RUSHDOWN),
    Card(ERUPTION),
    Card(INSIGHT)
])

flash_deck = Deck([
    Card(FLASH_OF_STEEL),
    Card(FLASH_OF_STEEL),
    Card(ERUPTION)
])
