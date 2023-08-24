from durak.game import Game
from durak.deck import Deck
from durak.player import Player
from durak.utils import create_game


def test_create_game_builder():
    game = create_game(player_1_name="Igor", player_2_name="Yura")
    assert type(game) == Game
    assert type(game.deck) == Deck
    assert game.deck.size() == 24
    
    assert type(game.player_1) == Player
    assert game.player_1.name == "Igor"
    assert game.player_1.deck.size() == 6
    
    assert type(game.player_2) == Player
    assert game.player_2.name == "Yura"
    assert game.player_2.deck.size() == 6
    