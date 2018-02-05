#!/usr/bin/env python3

def product(l):
    tmp = 1
    for i in l:
        tmp *= i
    return tmp

def check(m, l):
    return m == None or min(l) < m

def maxed(l):
    return product(l) > sum(l)

def increment(digits, minimum):
    digits[-1] += 1
    if maxed(digits):
        tmp = digits[:-1]
        increment(tmp, minimum)
        digits = tmp[:] + tmp[-1]
    return digits

for tmp in range(2, 12):
    digits = [1] * (tmp-2) + [2] * 2
    minimum = None
    while minimum == None or min(digits) < minimum:
        if product(digits) == sum(digits) and (minimum == None or minimum > sum(l)):
            minimum = sum(digits)
        print(minimum, digits)
        increment(digits, minimum)
        print(digits)
        
    else:
        print(tmp, m)


