from random import choice
from deck import *

class Move():

    #0 = stand, 1,2,3 = discard value 1,2,3 from hand
    moves = [0,1,2,3]


#abstract class for all players
class Player():

    def __init__(self,name):
        self.name = name
        self.hand = []

    def draw_card(self,num,deck):
        self.hand.append(deck.draw(num))

    def check_moves(self):
        possible_mvs = []

        #no matter what you can choose to stand regardless of your hand
        possible_mvs = Move.moves[0]

        #if we have the value of one in our hand we can discard it if we choose etc..

        if(Card.value[0] in self.hand):
            possible_mvs.append(Move.moves[1])

        if (Card.value[1] in self.hand):
            possible_mvs.append(Move.moves[2])

        if (Card.value[2] in self.hand):
            possible_mvs.append(Move.moves[3])

        #return a list of potential moves
        return(possible_mvs)

    #function called if we want to stand
    def stand(self):
        return Move.moves[0]

    #function called if we wish to discard cards
    def discard_one(self,card,deck):
        self.hand.remove(card)
        self.draw_card(1,deck)
        return Move.moves[1]

    def discard_two(self,card,deck):
        self.hand.remove(card)
        self.draw_card(1,deck)
        return Move.moves[2]

    def discard_three(self,card,deck):
        self.hand.remove(card)
        self.draw_card(1,deck)
        return Move.moves[3]

    def current_hand(self):
        #variables representing each card in the players hand
        c1 = self.hand[0]
        c2 = self.hand[1]

        #if we have a pair return the value of the pair
        if c1 == c2:
            if c1 == 3 and c2 == 3:
                return Score.pairs[2]
            if c1 == 2 and c2 == 2:
                return Score.pairs[1]
            if c1 == 1 and c2 == 1:
                return Score.pairs[0]

        #if no pairs, return the sum
        else:
            return c1+c2

#Random Randy makes random moves
class Randy(Player):

    def play(self,deck):
        #get our potential moves
        moves = self.check_moves()

        #select a random action from our potential moves
        action = choice(moves)

        #if our choice is stand we do so, else we randomly discard
        if action == moves[0]:
            return self.stand()

        else:
            return self.discard(choice(self.hand),deck)


#Don't discard if you have a pair, discard a one, or stand
class DeepPreschooler(Player):
    def play(self,deck):
        pairs = Score.pairs

        hand_score = self.current_hand()

        #if we do nto have a pair, discard 1, or stand if we do not have a 1
        if hand_score not in pairs:
            if 1 in self.hand:
                return self.discard(1,deck)
            else:
                return self.stand()

#always discards smallest value
class OddBall(Player):
    def play(self, deck):

        #discard the minimum value in our hand
        return self.discard(min(self.hand),deck)

class RLearner(Player):

    #will default to a learning rate of 0.1

    def __init__(self,name,rate = 0.1):
        #set name, learning rate, and the potential states
        super(RLearner, self).__init__(name)
        self.learning_rate = rate

        #States are    3,3    2,2   1,1   2,1   3,1   3,2
        self.states = [set([Card.value[2],Card.value[2]]),set([Card.value[1],Card.value[1]]),set([Card.value[0],Card.value[0]]),
                       set([Card.value[0],Card.value[1]]),set([Card.value[0],Card.value[2]]),set([Card.value[1],Card.value[2]])]

        #create a dictionary of weights for each state we have a different weight, begin at 0.5 for each
        self.weights = {
                            self.states[0]: 0.5,
                            self.states[1]: 0.5,
                            self.states[2]: 0.5,
                            self.states[3]: 0.5,
                            self.states[4]: 0.5,
                            self.states[5]: 0.5
                        }



    def play(self,deck):
        #list of valid next states
        next_states = set(self.states) & set(self.hand)
        prob = []

        for p in self.weights.items():
            if p[0] in next_states:
                prob.append(p)

        #sort probabilities
        prob = sorted(prob, key=lambda p: p[1])

        #set the best state to the highest probability
        best_state = prob[-1]

        if best_state[1] > self.weights[set(self.hand)]:
            cards = set(self.hand) - best_state[0]

            #get rid of your worst card (lowest value)
            dis_card = min(list(cards))
            return self.discard(dis_card,deck)

        #stand if you best possible state is worse than what you have
        else:
            return self.stand()



    #change the weight for the given state based on our reward or consequence of our action
    def learn(self,state,r):
        self.weights[state] = self.weights[state] + (self.learning_rate * (r-self.weights[state]))
