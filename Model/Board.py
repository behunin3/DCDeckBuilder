from Deck import Deck


class Board:
    def __init__(self, size):
        self.kick_deck = Deck()
        self.weakness_deck = Deck()
        self.super_villain_deck = Deck()
        self.line_up = []
        self.main_deck = Deck()