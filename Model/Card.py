from CardType import CardType

class Card:
    def __init__(self, 
            name: str, 
            description: str,
            cardType: CardType,
            cost: int,
            power: int,
            vp: int,
            draw_cards = 0,
            discards = 0
        ):
        self._name = name
        self._description = description
        self._type = cardType
        self._cost = cost
        self._power = power
        self._vp = vp
        self._draw_cards = draw_cards
        self._discards = discards
        self._has_played = False

    def getCost(self):
        return self._cost
    
    def play(self):
        if self._has_played:
            raise Exception("Card has already been played")
        self._has_played = True
        return self.draw_cards, self._power, 
    

