import random

class Deck:

    cards = [1,2,3,4]

    def __int__(self):
        cards = self.cards

    #simulates drawing a card from an infinitely large deck
    def draw(self):
        return random.choice(self.cards)



