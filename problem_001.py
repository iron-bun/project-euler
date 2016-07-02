#!/usr/bin/env python3

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def find_multiples(max_val, dividend):
    ans = max_val//dividend
    ans = ans * (ans + 1)
    ans /= 2
    return ans * dividend

#find all the multiplus of three and five, minus the multiples of fifteen
#to avoid double counting
print(find_multiples(999, 3) + find_multiples(999, 5) - find_multiples(999,15))


