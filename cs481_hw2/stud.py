from deck import *
from player import *

#abstract poker class
class Pre_Poker(object):

    def __init__(self):
        self.deck = Deck()

    #makes printing each player's hands easier
    def print_hands(self, p1, p2):
        print(p1.name + " hand: " + str(p1.hand))
        print(p2.name + " hand: " + str(p2.hand))

    def play(self, p1, p2):
        #each player draws 2 cards
        p1.draw(2,self.deck)
        p2.draw(2,self.deck)

        self.print_hands(p1,p2)

    def get_winner(self, p1, p2):
        #whoever has the better score wins!
        if p1.current_hand()>p2.current_hand():
            return p1
        elif p1.current_hand()<p2.current_hand():
            return p2
        else:
            return None


class Stud(Pre_Poker):

    def play(self,p1,p2):
        #use the inherited play function
        super(Stud, self).play(p1,p2)

        #convert hands to sets
        cards1 = set(p1.hand)
        cards2 = set(p2.hand)


        if self.get_winner(p1,p2) is p1:
            #if player one is the learner we call learn with our state and make our reward 1 to improve the weight
            if type(p1) == "RLearner":
                p1.learn(cards1, 1)

            #if it's not the learner, we send it a 0 reward, thus making this hand less favorable
            else:
                p2.learn(cards2,0)
            print(p1.name + "wins")
            return 1

        elif self.get_winner(p1,p2) is p2:
            if type(p2) == "RLearner":
                p2.learn(cards2, 1)
            else:
                p1.learn(cards1,0)

            print(p2.name + " wins")
            return 0
        #if we tie we leave the learner as is
        else:
            print("Tie")
            return 0

