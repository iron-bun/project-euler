#!/usr/bin/env python3

#https://projecteuler.net/problem=84

#Rules:
#Three doubles goes to jail and resets the doubles count
#No other go-to-jail method resets the doubles count
#The probabilites shown on the question page are truncated to three significant figures, not rounded

#Notes:
#It is possible to get these rules wrong and still end up with an answer that is close enough

import numpy as np

die = [1,2,3,4]
throws = [(i,j) for i in die for j in die] 

#Initialise Markov chain to zero
states = [[0 for i in range(120)] for board in range(120)]

#Add all of the possible destinations from the current start square
for start, board in enumerate(states):

    for throw in throws:
          destination = start+throw[0]+throw[1]
          if destination//40 > start//40:
              destination -= 40

          if throw[0] == throw[1]:
              destination += 40
          else:
              destination %= 40

          if destination >= 120:
              destination = 10

          board[destination] += 1

#skew the boards to account for chance, community chest and go to jail
for board in states:
    #go to jail
    for square in [30, 70, 110]:
        offset = (square // 40) * 40
        board[offset+10] += board[square]
        board[square] = 0

    #chance cards
    for square in [7, 47, 87, 22, 62, 102, 36, 76, 116]:
        offset = (square // 40) * 40
        board[offset]    += board[square] / 16     #advance to go
        board[offset+10] += board[square] / 16     #go to jail
        board[offset+11] += board[square] / 16     #advance to C1
        board[offset+24] += board[square] / 16     #advance to E3
        board[offset+39] += board[square] / 16     #advance to H3
        board[offset+5]  += board[square] / 16     #advance to R1
        board[square-3]  += board[square] / 16     #go back 3 spaces

    for square in [7, 47, 87]:
        offset = (square // 40) * 40
        board[offset+15] += board[square] * 2 / 16 #advance to next R
        board[offset+12] += board[square] / 16     #advance to next U

    for square in [22, 62, 102]:
        offset = (square // 40) * 40
        board[offset+25] += board[square] * 2 / 16 #advance to next R
        board[offset+28] += board[square] / 16     #advance to next U

    for square in [36, 76, 116]:
        offset = (square // 40) * 40
        board[offset+5]  += board[square] * 2 / 16 #advance to next R
        board[offset+12] += board[square] / 16     #advance to next U

    for square in [7, 47, 87, 22, 62, 102, 36, 76, 116]:
        board[square]    *= 6 / 16                 #stay on square

    #community chest cards
    for square in [2, 17, 33, 42, 57, 73, 82, 97, 113]:
        offset = (square // 40) * 40
        board[offset]    += board[square] / 16 #advance to Go
        board[offset+10] += board[square] / 16 #go to jail
        board[square]    *= 14 / 16            #stay on square

    #Normalise all the probabilities to sum to 1
    for square in range(120):
        board[square] /= len(throws)

start = states[0]

for i in range(500):
  start = np.dot(start, states)

start = [start[i] + start[i+40] + start[i+80] for i in range(40)]
for i, j in sorted(enumerate(start), key=lambda p: p[1]):
  print(i, j)

