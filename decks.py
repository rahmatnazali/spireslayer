from typing import Optional

from card import Card


class Deck():
    def __init__(self, card_list: Optional[list] = None) -> None:
        super().__init__()

        if card_list is not None:
            self.card_list = card_list
        else:
            self.card_list = []

    def add_card(self, card: Card):
        self.card_list.append(card)

    def to_json(self):
        return [
            card.to_json() for card in self.card_list
        ]


defect_lightning_deck = Deck([
    Card(Card.LEAP),
    Card(Card.LEAP),
    Card(Card.LEAP),
    Card(Card.ZAP),
    Card(Card.ZAP),
    Card(Card.ZAP),
    Card(Card.ZAP),
    Card(Card.DEFRAGMENT),
    Card(Card.DEFRAGMENT),
    Card(Card.DEFRAGMENT),
    Card(Card.DEFRAGMENT),
    Card(Card.THUNDER_STRIKE),
])

defect_frost_deck = Deck([
    Card(Card.GLACIER),
    Card(Card.GLACIER),
    Card(Card.GLACIER),
    Card(Card.DEFRAGMENT),
    Card(Card.DEFRAGMENT),
    Card(Card.DEFRAGMENT),
    Card(Card.BLIZZARD),
    Card(Card.BLIZZARD),
    Card(Card.BLIZZARD),
    Card(Card.BLIZZARD),
    Card(Card.BLIZZARD),
])
