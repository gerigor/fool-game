from copy import deepcopy
from durak.card import Card


class Deck:
    def __init__(self) -> None:
        self.cards = []
    
    def size(self) -> int:
        return len(self.cards)

    def add_card(self, card: Card):
        self.cards.append(card)

    def take_card_from_top(self) -> Card:
        try:
            return self.cards.pop(0)
        except IndexError:
            raise NoCardInDeckError("No more cards in deck")


class NoCardInDeckError(Exception):
    pass
