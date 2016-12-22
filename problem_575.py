#!/usr/bin/env python3
#https://projecteuler.net/problem=575

import numpy as np

def print_chain(chain):
    for i in range(5):
        print(chain[i*5:(i*5)+5])

def calculate_probability(chain, square, mode):
    options = 4
    if square%grid_size == 0 or square%grid_size == grid_size-1:
        options-=1

    if square < grid_size or square >= grid_size**2 - grid_size:
        options-=1

    populate(chain, square, mode, options)

def populate(chain, square, mode, options):
    if mode:
        chain[square] += 0.5
        probability = 0.5/options
    else:
        probability = 1/(options+1)
        chain[square] += probability

    if square%grid_size > 0:
        chain[square-1] += probability
    if square%grid_size < grid_size-1:
        chain[square+1] += probability
    if square >= grid_size:
        chain[square-grid_size] += probability
    if square < grid_size**2-grid_size:
        chain[square+grid_size] += probability

def normalise(chain):
    total = sum(chain)
    for idx,square in enumerate(chain):
        chain[idx] = square*1/total

def get_total(chain, mode):
    for idx, c in enumerate(chain):
        calculate_probability(c, idx, mode)
    for c in chain:
        normalise(c)

    start = chain[0][:]
    for i in range(500):
        start = np.dot(start, chain)

    ans = 0
    for idx, square in enumerate(start):
        if (idx+1)**0.5 == int((idx+1)**0.5):
            ans += square
    return ans

grid_size = 5

markov_chain1 = [[0 for i in range(grid_size**2)] for i in range(grid_size**2)]
ans = get_total(markov_chain1, True)/2

markov_chain2 = [[0 for i in range(grid_size**2)] for i in range(grid_size**2)]
ans += get_total(markov_chain2, False)/2

print(ans)
