
#main

import random
from deck import Deck
from player import PlayerA
from player import PlayerC
#tracking the probability of each state
pA = [0,0,0,0,0]
pC = [0,0,0,0,0]

p1 = PlayerC("dealer")
p2 = PlayerA("dealer")
games = 10
#simulates
iteration = games

while games>0:
    while p1.choose()!=-1:
        if(p1.state == 1):
            pC[0] += 1
        elif (p1.state == 2):
            pC[1] +=1
        elif (p1.state == 3):
            pC[2]+=1
        elif (p1.state == 4):
            pC[3]+=1
        elif (p1.state > 4):
            pC[4]+=1
games = iteration
while games > 0:
    while p2.choose() != -1:
        if (p2.state == 1):
            pA[0] += 1
        elif (p2.state == 2):
            pA[1] += 1
        elif (p2.state == 3):
            pA[2] += 1
        elif (p2.state == 4):
            pA[3] += 1
        elif (p2.state > 4):
            pA[4] += 1
    games-=1
    p1.reset()

print("Via sampling/simulation the stationary probabilities are:\n")
i=0
while i<len(pC):
    pC[i] = float(pC[i]/iteration)
    i+=1
while i<len(pC):
    pA[i] = float(pA[i]/iteration)
    i+=1


