from collections import deque
import random
import time

class Deck:
    def __init__(self):
        self.cards = deque()

    def __len__(self):
        return len(self.cards)

    def draw(self):
        if self.cards:
            return self.cards.popleft()
        else:
            return None
        
    def add(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.seed(time.time())
        lst = list(self.cards)
        random.shuffle(lst)
        self.cards = deque(lst)

    def peek(self):
        top_card = self.cards[0] if self.cards else None
        return top_card
    
    def clear(self):
        self.cards.clear()

    def remove(self, card):
        lst = list(self.cards)
        if card in lst:
            lst.remove(card)
            self.cards = deque(lst)
        else:
            raise Exception("Card not found in deck")