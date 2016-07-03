#!/usr/bin/env python3

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

import primes

count = 0
for i in primes.primes(200000):
    count += 1
    if count == 10001:
        print(i)
        exit()
