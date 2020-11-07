from player import PlayerA
from player import PlayerC
import random


states = [0,1,2,3,4,5]

transitions = ["start->1","start->2","start->3","start->4","start->Bust",
               "1->2","1->3","1->4","1->Bust",
               "2->3","2->4","2->Bust",
               "3->4","4->Bust"]

transition_matrixA= [[0,0,0,0,0,0],
                     [0,0,0,0,0,0],
                     [0,0,0,0,0,0],
                     [0,0,0,0,0,0],
                     [0,0,0,0,0,0],
                     [0,0,0,0,0,0]]

transition_matrixC= [[0,0,0,0,0,0],
                     [0,0,0,0,0,0],
                     [0,0,0,0,0,0],
                     [0,0,0,0,0,0],
                     [0,0,0,0,0,0],
                     [0,0,0,0,0,0]]

p1 = PlayerC("dealer")
p2 = PlayerA("dealer")

#a list of the states
games = 10
state_l = []
iteration = 10
while games > 0:
    while p1.choose() != -1:
        state_l.append(p1.state)
    games-=1
    p1.reset()
    print(state_l)
    i=0
    while i < len(state_l):
        for j in state_l[i:]:
            if(j == 1):
                transition_matrixC[i][1]+=1
            elif (j == 2):
                transition_matrixC[i][2] += 1
            elif (j == 3):
                transition_matrixC[i][3] += 1
            elif (j == 4):
                transition_matrixC[i][4] += 1
            elif (j > 4):
                transition_matrixC[i][5] += 1
        i+=1
    state_l = []

i=0
while i < len(transition_matrixC):
    j=0
    while j < len(transition_matrixC[i]):
        transition_matrixC[i][j] = float(transition_matrixC[i][j]/iteration)
        j+=1
    i+=1

print(transition_matrixC)








