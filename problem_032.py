#!/usr/bin/env python3

#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
#The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

import itertools

digits = list("123456789")

ans = {}
for combination in itertools.permutations(digits):
    if int("".join(combination[0:1])) * int("".join(combination[1:5])) == int("".join(combination[5:])):
        ans[int("".join(combination[5:]))] = 1
    if int("".join(combination[0:2])) * int("".join(combination[2:5])) == int("".join(combination[5:])):
        ans[int("".join(combination[5:]))] = 1

print(sum(ans.keys()))
