from durak.deck import Deck

class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.deck = Deck()
