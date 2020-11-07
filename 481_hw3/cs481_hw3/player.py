from deck import Deck

#Standard Player, Policy A
class PlayerA:

    def __init__(self,name):
        self.name = name
        self.hand = []
        self.busted = False
        self.state = 0
        self.deck = Deck()

    def choose(self):
        if (self.state < 4):
            self.hit()
            return 0
        elif (self.busted == True):
            #print(str(self.name) + " has busted\nFinal hand " + str(self.hand))
            return -1
        else:
            #print(str(self.name) + " stands\nFinal hand:" + str(self.hand))
            return -1

    def hit(self):
        #print(str(self.name) + " hits")
        self.hand.append(self.deck.draw())
        self.state = sum(self.hand)
        if self.state>4:
            self.busted = True

    def reset(self):
        self.state = 0
        self.hand = []
        self.busted = False

#GrayJack Player, Policy C
class PlayerC:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.busted = False
        self.state = 0
        self.deck = Deck()

    def hit(self):
        self.hand.append(self.deck.draw())
        self.state = sum(self.hand)

        #print(str(self.name) + " hits\tcurrent hand:" + str(self.hand))
        if self.state > 4:
            self.busted = True
            return



    def choose(self):
        if(self.state<=2):
            self.hit()
            return 0
        elif(self.busted == True):
            #print(str(self.name) + " has busted\nFinal hand " + str(self.hand))
            return -1
        else:
            #print(str(self.name) + " stands\nFinal hand:" + str(self.hand))
            return -1

    def reset(self):
        self.state = 0
        self.hand = []
        self.busted = False

