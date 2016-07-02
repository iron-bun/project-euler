#!/usr/bin/env python3

def prime_factors(val):
    ans = {}
    divisor = 2
    while val > divisor:
        if val % divisor == 0:
            ans[divisor] = ans.get(divisor, 0) + 1
            val //= divisor
        else:
            divisor += 1
    if val > 1:
        ans[val] = ans.get(divisor, 0) + 1
    return ans

factors = {}
for i in range(2, 21):
    tmp = prime_factors(i)
    for j in tmp.keys():
        if tmp[j] > factors.get(j, 0):
            factors[j] = tmp[j]


ans = 1
for i in factors:
    ans *= (i ** factors[i])

print(ans)
