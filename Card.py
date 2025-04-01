from CardType import CardType

class Card:
    def __init__(self, cardType: CardType):
        self._name = None
        self._description = None
        self._type = cardType
        self._cost = None
        self._power = None
        self._defense = None
        self._attack = None

    def getCost(self):
        return self._cost
    

