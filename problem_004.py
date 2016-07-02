#!/usr/bin/env python3

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(val):
    tmp = str(val)
    return tmp == tmp[::-1]

ans = 0
for i in reversed(range(100, 1000)):
    for j in reversed(range(i, 1000)):
        if is_palindrome(i*j) and i*j > ans:
            ans = i * j
        if i * j < ans:
            break

print(ans)
