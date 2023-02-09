

class Card(object):
    def __init__(self, id: str, misc: int = 0, upgrades: int = 1) -> None:
        super().__init__()
        self.id = id
        self.misc = misc
        self.upgrades = upgrades

    def to_json(self):
        return {
            "id": self.id,
            "misc": self.misc,
            "upgrades": self.upgrades
        }
