#!/usr/bin/env python3

#https://projecteuler.net/problem=203

import primes

def pascals_triangle(depth):
    triangle = [[1]]

    for i in range(depth-1):
        last_row = triangle[-1]
        tmp = [1]
        for a, b in zip(last_row, last_row[1:]):
            tmp.append(a+b)
        tmp.append(1)
        triangle.append(tmp)
    return triangle

def prime_squares(primes):
    return [p**2 for p in primes]

digits = set()
for i in pascals_triangle(51):
    for j in i:
        digits.add(j)

p_squares = prime_squares(primes.primes(int(max(digits)**0.5)))

ans = 0
for d in digits:
    for ps in p_squares:
        if d%ps == 0:
            break
    else:
        ans += d

print(ans)
