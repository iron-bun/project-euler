#!/usr/bin/env python3

#https://projecteuler.net/problem=67


with open("data/p067_triangle.txt") as f:
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
 
