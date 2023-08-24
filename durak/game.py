from durak.deck import Deck
from durak.player import Player


class Game:
    def __init__(self, deck: Deck, player_1: Player, player_2: Player) -> None:
        self.deck = deck        
        self.player_1 = player_1
        self.player_2 = player_2

    def draw_cards_to_player(self, player_name, cards_count):
        if self.player_1.name == player_name:
            player = self.player_1
        elif self.player_2.name == player_name:
            player = self.player_2

        for _ in range(cards_count):
            card = self.deck.take_card_from_top()  # Take one card from deck
            player.deck.add_card(card)  # Give this to player

    # def next_turn(self):
    #     yield 1
    #     yield 2
    #     yield 3
