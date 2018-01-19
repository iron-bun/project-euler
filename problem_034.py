#!/usr/bin/env python3

#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial

factorials = [factorial(i) for i in range(10)]

def fact_sum(n):
    return sum(factorials[int(i)] for i in str(n))

#TODO: work out where the cap is
if __name__ == '__main__':
    print(sum(i for i in range(10,1000000) if i == fact_sum(i)))
