#!/usr/bin/env python3

#A hexagonal orchard of order n is a triangular lattice made up of points within a regular hexagon with side n. The following is an example of a hexagonal orchard of order 5:
#
#p351_hexorchard.png
#Highlighted in green are the points which are hidden from the center by a point closer to it. It can be seen that for a hexagonal orchard of order 5, 30 points are hidden from the center.
#
#Let H(n) be the number of points hidden from the center in a hexagonal orchard of order n.
#
#H(5) = 30. H(10) = 138. H(1 000) = 1177848.
#
#Find H(100 000 000).

#The visible trees are the ones with co-ordinates with co-prime values
#The hexagon can be divided into six identical shapes. Each triangle can be skewed into a square with easy co-ordinates.

# 100,000,000 means 500,000,005,000,000 points to check individually
# A whole row can be checked using the same solution as problem 1. Add up the count of primes and discount the composite factors.
# 100,000,000 rows is still too many to do one at a time. Half the rows by using the relective symetry in the triangle.

# The whole grid is a triangle number of that size so we can work out the whole grid for one prime in one calculation. Then we pick combinations from the available primes to only calculate for unique grids.

# Something not covered in problem 1 is if we want all the number divisble by 2, 3 and 5. There are three ways to reach 30 but four ways to make 30 out of combinations or 2, 3 and 5. It becomes a net negative. Correcting for this means re-adding the odd length prime combinations.

import primes

def product(n):
    ans = 1
    for v in n:
        ans *= v
    return ans

def triangle(n):
    return n * (n+1) // 2

def combos(values, max_product, pos=0):
    for i in range(pos, len(values)):
        tmp = values[i]
        if tmp > max_product:
            return
        yield [tmp]
        for v in combos(values,max_product//tmp, i+1):
            yield [tmp] + v 

def solve(n):
    ans = n-1

    prime_list = primes.primes(int(n))
    for i in combos(prime_list, n):
        tmp = product(i)
        tmp = triangle((n-tmp)//tmp)
        if len(i) % 2 == 0:
            ans -= tmp 
        else:
            ans += tmp
    return ans * 6

if __name__ == '__main__':
    tests = [5, 10, 1000, 100000000]
    for i in tests:
        ans = solve(i)
        print(i, ans)

