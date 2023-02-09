

class Card(object):
    STRIKE = "Strike_B"
    DEFEND = "Defend_B"

    LEAP = "Leap"
    DUALCAST = "Dualcast"
    DEFRAGMENT = "Defragment"
    CAPACITOR = "Capacitor"

    # lightning
    ZAP = "Zap"
    THUNDER_STRIKE = "Thunder Strike"

    # ice
    COLD_SNAP = "Cold Snap"
    BLIZZARD = "Blizzard"
    GLACIER = "Glacier"

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
