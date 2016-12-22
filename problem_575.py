#!/usr/bin/env python3
#https://projecteuler.net/problem=575

import numpy as np
import scipy as sp
from scipy.sparse import csr_matrix

def populate(square, row_ind, col_ind, data, mode):
    options = 4
    if square%grid_size == 0 or square%grid_size == grid_size-1:
        options-=1

    if square < grid_size or square >= grid_size**2 - grid_size:
        options-=1

    row_ind.append(square)
    col_ind.append(square)
    if mode:
        data.append(0.5)
        probability = 0.5/options
    else:
        probability = 1/(options+1)
        data.append(probability)

    if square%grid_size > 0:
        row_ind.append(square)
        col_ind.append(square-1)
        data.append(probability)
    if square%grid_size < grid_size-1:
        row_ind.append(square)
        col_ind.append(square+1)
        data.append(probability)
    if square >= grid_size:
        row_ind.append(square)
        col_ind.append(square-grid_size)
        data.append(probability)
    if square < grid_size**2-grid_size:
        row_ind.append(square)
        col_ind.append(square+grid_size)
        data.append(probability)

def get_total(chain):

    start = csr_matrix(([1], ([0], [0])), shape=(1, grid_size**2))
    for i in range(500):
        start = sp.dot(start, chain)

    ans = 0
    start = start.toarray()[0]

    for idx, square in enumerate(start):
        if (idx+1)**0.5 == int((idx+1)**0.5):
            ans += square
    return ans

grid_size = 5
row_ind = []
col_ind = []
data = []

for i in range(grid_size**2):
    populate(i, row_ind, col_ind, data, True)

sparse_chain = csr_matrix((data, (row_ind, col_ind)), shape=(grid_size**2, grid_size**2))
ans = get_total(sparse_chain)/2

row_ind = []
col_ind = []
data = []

for i in range(grid_size**2):
    populate(i, row_ind, col_ind, data, False)

sparse_chain = csr_matrix((data, (row_ind, col_ind)), shape=(grid_size**2, grid_size**2))
ans += get_total(sparse_chain)/2

print(ans)
