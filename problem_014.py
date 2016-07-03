#!/usr/bin/env python3

#The following iterative sequence is defined for the set of positive integers:

#n → n/2 (n is even)
#n → 3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:

#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

#Which starting number, under one million, produces the longest chain?

#NOTE: Once the chain starts the terms are allowed to go above one million.

cache = {}
def collatz(n):
    if n in cache:
        return cache[n]

    tmp = n
    counter = 1
    while tmp % 2 == 0:
        tmp //= 2
        counter += 1
    if tmp > 1: 
        counter += collatz(3*tmp + 1)
    cache[n] = counter
    return counter

ans = 0
max_len = 0
for i in range(1, 1000000):
    tmp = collatz(i)
    if tmp > max_len:
        (ans, max_len) = (i, tmp)

print(ans)
