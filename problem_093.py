#!/usr/bin/env python3

#By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.

#For example,

#8 = (4 * (1 + 3)) / 2
#14 = 4 * (3 + 1 / 2)
#19 = 4 * (2 + 3) − 1
#36 = 3 * 4 * (2 + 1)

#Note that concatenations of the digits, like 12 + 34, are not allowed.

#Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

#Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.

#combine digits and operators in all possible ways
#Using reverse notation instead of parentheses because that's easier to write.

import itertools

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

operators = {'+': add, '-': subtract, '*':multiply, '/':divide}

digits = [1,2,3,4,5,6,7,8,9]

def evaluate(calculation):
    #print(calculation)
    stack = []
    try:
        for c in calculation:
            if c not in operators:
                stack.append(c)
            else:
                tmp = operators[c](stack.pop(), stack.pop())
                stack.append(tmp)
    except:
        return 0
    return stack[0]
 

def combine(digits, operators):
    results = set()
    for d in itertools.permutations(digits):
        for o in unique(itertools.permutations(list(operators)*3, 3)):
            # There are only two basic calculations:
            #  ddsddss OR ddddsss
            # Any calculation of the style ddsdsds or dddsdss can be represented by ddddsss with a different permutation of digits
            calculation = d + o
            tmp_result = evaluate(calculation)
            if tmp_result > 0 and tmp_result % 1 == 0:
                results.add(tmp_result)
            calculation = d[:2] + tuple(o[0]) + d[2:] + o[1:]
            tmp_result = evaluate(calculation)
            if tmp_result > 0 and tmp_result % 1 == 0:
                results.add(tmp_result)

    return sorted(map(int,results))
    
def unique(iterator):
    seen = []
    for it in iterator:
        if it in seen:
            continue
        seen.append(it)
        yield it

def solve():
    ans = 0
    ans_max = 0
    for digit_combination in itertools.combinations(digits, 4):
        tmp = combine(digit_combination, operators)
        index = 1
        count = 0
        print("'"+"".join(map(str,digit_combination)), tmp)
        for i in map(int,tmp):
            if i < 1:
                continue
            if i == index:
                count+=1
                index+=1
            else:
                break
        
        if count >= ans_max:
            ans = "".join(map(str,sorted(digit_combination)))
            ans_max = count
    print(ans, ans_max)

if __name__ == '__main__':
    solve()
