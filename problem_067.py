#!/usr/bin/env python3

#By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

#3
#7 4
#2 4 6
#8 5 9 3
#
#That is, 3 + 7 + 4 + 9 = 23.
#
#Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
#
#NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

with open('data/p067_triangle.txt') as f:
    rows = f.readlines()

prev_row = [int(i) for i in rows[0].split()]

for row in rows[1:]:
   new_row = [int(i) for i in row.split()]
   new_row[0] += prev_row[0]
   for i in range(len(new_row) - 2):
       new_row[i+1] += max(prev_row[i], prev_row[i+1])
   new_row[-1] += prev_row[-1]
   prev_row = new_row

print(max(prev_row))
 
