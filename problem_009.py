#!/usr/bin/env python3

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def pythagorean_triple(m, n):
    return (m**2 - n**2, 2 * m * n, m**2 + n**2)

def find_triple():
    i = 0
    while True:
        i += 1
        j = i 
        while True:
            j += 1
            (a, b, c) = pythagorean_triple(j, i)
            if a + b + c == 1000:
                return (a, b, c)
            elif a + b + c > 1000:
                break

(a, b, c) = find_triple()
print(a*b*c)
