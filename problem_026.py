#!/usr/bin/env python3

#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
#1/2	= 	0.5
#1/3	= 	0.(3)
#1/4	= 	0.25
#1/5	= 	0.2
#1/6	= 	0.1(6)
#1/7	= 	0.(142857)
#1/8	= 	0.125
#1/9	= 	0.(1)
#1/10	= 	0.1
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def reciprocal_cycle(n):
    remainder = 1
    count = 0
    remainders = [0,1]
    while True:
        while remainder < n:
            remainder *= 10
        remainder %= n
        count += 1
        if remainder in remainders:
            break
        remainders.append(remainder)
    if remainder == 0:
        return 0
    return count

ans = 0
max_len = 0
for i in range(1, 1000):
    tmp = reciprocal_cycle(i)
    if tmp > max_len:
        ans, max_len = i, tmp

print(ans)
