#!/usr/bin/env python3

#https://projecteuler.net/problem=5

import primes

prime_list = primes.primes(20)

factors = {}
for i in range(2, 21):
    tmp = primes.prime_factors(i, prime_list)
    tmp = { x: tmp.count(x) for x in set(tmp) }
    for j in tmp.keys():
        if tmp[j] > factors.get(j, 0):
            factors[j] = tmp[j]


ans = 1
for i in factors:
    ans *= (i ** factors[i])

print(ans)
