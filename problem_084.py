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

def goto_jail(square, board, value):
    offset = (square // 40) * 40
    increment(offset + 10, board, value)

def chance_card(square, board, value):
    offset   = (square//40) * 40

    increment(offset, board, value/16)
    goto_jail(square, board, value/16)
    increment(offset+11, board, value/16)
    increment(offset+24, board, value/16)
    increment(offset+39, board, value/16)
    increment(offset+5,  board, value/16)
    increment(square-3,  board, value/16)

    if square in [7, 47, 87]:
        increment(offset+15, board, value * 2 / 16)
        increment(offset+12, board, value / 16)

    if square in [22, 62, 102]:
        increment(offset+25, board, value * 2 / 16)
        increment(offset+28, board, value / 16)

    if square in [36, 76, 116]:
        increment(offset+5, board, value * 2 / 16)
        increment(offset+12, board, value / 16)

    board[square] += value * 6 / 16

def community_chest_card(square, board, value=1):
    offset = (square // 40) * 40
    increment(offset, board, value/16)
    goto_jail(square, board, value/16)
    board[square] += value * 14 / 16

cards = {
    2:  community_chest_card,
    7:  chance_card,
    17: community_chest_card,
    22: chance_card,
    30: goto_jail,
    33: community_chest_card,
    36: chance_card
}

def increment(square, board, value):
    action = cards.get(square%40, None)

    if action == None:
        board[square] += value
    else:
       action(square, board, value)
 

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

          increment(destination, board, 1)

    #Normalise all the probabilities to sum to 1
    for square in range(120):
        board[square] /= len(throws)

start = states[0]

for i in range(500):
    start = np.dot(start, states)

start = [start[i] + start[i+40] + start[i+80] for i in range(40)]
for i, j in sorted(enumerate(start), key=lambda p: p[1]):
    print(i, j)

