from random import *

#card values
class Card:
    value = [1,2,3]

#potential hand scores for a pair
class Score:
    pairs = [6,7,8]

#deck of cards
class Deck:
    cards = [Card.value[0],Card.value[0],Card.value[0],
             Card.value[1],Card.value[1],Card.value[1],
             Card.value[2],Card.value[2],Card.value[2]]


    #reset the deck with every new instance
    def __int__(self):
        self.cards = [Card.value[0],Card.value[0],Card.value[0],
             Card.value[1],Card.value[1],Card.value[1],
             Card.value[2],Card.value[2],Card.value[2]]

        shuffle(self.cards)

    #draw 1 or n cards from the deck
    def draw(self, n=1):
        self.drawn = []
        #for each card we draw take a card from the top, and add it to our new cards
        for i in range(n):
            self.drawn.append(self.cards.pop())
        return self.drawn
