from durak.card import Card
from durak.game import Game
from durak.deck import Deck
from durak.player import Player


def test_game_create():
    deck = Deck()
    game = Game(deck, Player("name_1"), Player("name_2"))
    
    assert type(game) == Game


def test_game_draw_cards_to_player():
    deck = Deck()
    game = Game(deck, Player("name_1"), Player("name_2"))
    
    game.deck.add_card(Card('spades', 'ace'))
    game.deck.add_card(Card('spades', '6'))
    game.deck.add_card(Card('spades', '7'))
    
    game.draw_cards_to_player("name_1", 2)

    assert game.deck.size() == 1
    assert game.player_1.deck.size() == 2
