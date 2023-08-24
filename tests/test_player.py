
import pytest
from durak.deck import Deck

from durak.player import Player


@pytest.mark.parametrize("name", ["John", "Jane"])
def test_game_create(name):
    player = Player(name=name)
    assert type(player) == Player
    assert player.name == name
    assert type(player.deck) == Deck
