from collections import deque
import random

class Deck:
    def __init__(self):
        self.cards = deque()

    def draw(self):
        if self.cards:
            return self.cards.popleft()
        else:
            return None
        
    def add(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)