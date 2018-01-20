#!/usr/bin/env python3

#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#(Please note that the palindromic number, in either base, may not include leading zeros.)

def generate_palindromes(i):
    tmp = str(i)
    value_1 = tmp + tmp[-2::-1]
    value_2 = tmp + tmp[::-1]
    return int(value_1), int(value_2)

def base_2(i):
    return "{0:b}".format(i)

def is_palindrome(i):
    return i == i[::-1]

def return_if_binary_palindrome(i):
    if is_palindrome(base_2(i)):
        return i
    else:
        return 0

def main():
    ans = 0
    for i in range(1, 1000):
        value_1, value_2 = generate_palindromes(i)
        ans += return_if_binary_palindrome(value_1)
        ans += return_if_binary_palindrome(value_2)
    print(ans)

if __name__ == '__main__':
    main()
