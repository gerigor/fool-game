from durak.card import Card

def test_card_create():
    card = Card(suit='spades', rank='ace')
    assert type(card) == Card
    assert card.suit == 'spades'
    assert card.rank == 'ace'
