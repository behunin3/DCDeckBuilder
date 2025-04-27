from Card import Card
from Deck import Deck
class Player:
    def __init__(self, name, hero):
        self.name = name
        self.hand = []
        self.drawDeck = Deck()
        self.discards = Deck()
        self.victory_points = 0
        self.locations = []
        self.power = 0
        self.super_hero = hero

    def draw(self):
        if len(self.drawDeck) <= 0:
            self.shuffle()
        card: Card = self.drawDeck.draw()
        self.hand.append(card)

    def discard(self, card):
        self.hand.remove(card)
        self.discard.add(card)

    def destroy(self, card, card_location):
        if card_location == "hand":
            self.hand.remove(card)
        elif card_location == "deck":
            self.drawDeck.remove(card)
        elif card_location == "discard":
            self.discards.remove(card)
        else:
            raise Exception("Invalid card location")
        # return card

    def flipTopCard(self):
        card = self.drawDeck.peek()
        if card == None:
            self.shuffle()
            card = self.drawDeck.peek()
        return card

    def gain(self, card):
        self.discards.add(card)

    def buy(self, card: Card):
        cost = card.getCost()
        if cost > self.power:
            raise Exception("Not enough power to buy this card")
        self.power -= cost
        self.discards.add(card)


    def play(self, card: Card):
        draw_card, power, attack = card.play()

    def shuffle(self):
        self.discards.shuffle()
        self.drawDeck = self.discards
        self.discards.clear()





