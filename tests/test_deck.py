import pytest
from durak.deck import Deck, NoCardInDeckError
from durak.card import Card


def test_deck_create():
    deck = Deck()
    assert type(deck) == Deck
    assert deck.size() == 0


def test_deck_add_card():
    card = Card('spades', 'ace')

    deck = Deck()
    deck.add_card(card)
    assert deck.size() == 1


def test_deck_take_card_from_top():
    deck = Deck()
    deck.add_card(Card('spades', 'ace'))

    card = deck.take_card_from_top()
    assert type(card) == Card
    assert deck.size() == 0



def test_deck_take_card_from_top_of_empty_deck():
    deck = Deck()
    with pytest.raises(NoCardInDeckError):
        deck.take_card_from_top()
