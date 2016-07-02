#!/usr/bin/env python3

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

target = 600851475143
divisor = 3

while target > divisor:
    if target % divisor != 0:
        divisor += 2
    else:
        target /= divisor

print(target)
