from durak.card import Card
from durak.game import Game
from durak.deck import Deck
from durak.player import Player


def create_game(player_1_name, player_2_name):
    deck = Deck()
    for suit in ['hearts', 'diamonds', 'clubs', 'spades']:
        for rank in ['6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']:
            deck.add_card(Card(suit=suit, rank=rank))

    player_1 = Player(player_1_name)
    player_2 = Player(player_2_name)
    
    game = Game(deck, player_1, player_2)

    game.draw_cards_to_player(player_1_name, 6)
    game.draw_cards_to_player(player_2_name, 6)

    return game
