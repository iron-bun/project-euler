#!/usr/bin/env python3

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

import primes

ans = sum(primes.primes(1999999))
print(ans)
