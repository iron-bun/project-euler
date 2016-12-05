#!/usr/bin/env python3

#https://projecteuler.net/problem=97

#The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.
#
#However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433*2^7830457+1.
#
#Find the last ten digits of this prime number.

#Note: Python can handle this as regular maths, but the below prevents it chewing up lots of ram.

ans = 28433
for i in range(7830457):
    ans *= 2
    ans %= 10000000000

print(ans+1)
