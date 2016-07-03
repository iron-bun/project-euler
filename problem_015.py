#!/usr/bin/env python3

#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?


def pascals_triangle():
    row = [1]
    while True:
        new_row = [1]
        for j in range(len(row)-1):
            new_row.append(row[j] + row[j+1])
        new_row.append(1)
        row = new_row
        yield row

grid_size = 20
for i in pascals_triangle():
    if len(i) > grid_size*2:
        ans = i
        break

print(ans[grid_size])
