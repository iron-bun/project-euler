#!/usr/bin/env python3

grid = {}
with open('data/p082_matrix.txt') as f:
    for y, line in enumerate(f):
        for x, val in enumerate(line.rstrip().split(",")):
            grid[(x, y)] = [int(val), None]

def neighbours(x, y):
    if x < 79:
        yield (x+1, y)
    if y > 0:
        yield (x, y-1)
    if y < 79:
        yield (x, y+1)

def search():
    open_set = [(0,y) for y in range(80)]
    for node in open_set:
        grid[node][1] = grid[node][0]

    while len(open_set) > 0:
       current_node = sorted(open_set, key=lambda x: grid[x][1])[0]
       open_set.remove(current_node)

       if current_node[0] == 79:
           return

       for (x, y) in neighbours(current_node[0], current_node[1]):
           if not grid[(x, y)][1] or grid[(x, y)][1] > grid[current_node][1] + grid[(x, y)][0]:
               grid[(x, y)][1] = grid[current_node][1] + grid[(x, y)][0]
               open_set.append((x, y))

search()
ans = None
for i in range(80):
    if not grid[(79,i)][1]:
        continue
    if not ans or ans > grid[(79,i)][1]:
        ans = grid[(79,i)][1]
print(ans)
