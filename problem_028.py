#!/usr/bin/env python3

#Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 12
#17 16 15 14 13

#It can be verified that the sum of the numbers on the diagonals is 101.

#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

#Naïve loop
#ans = 1
#inc = 0
#val = 1
#while inc < 1000:
    #inc += 2
    #for i in range(4):
        #val += inc
        #ans += val


#Quadratic series of above loop
#ans = sum([16*n**2 + 4*n + 4 for n in range(1,501)])+1

#Sum the quadratic series
n = 500
ans = 16*n*(n+1)*(2*n+1)//6
ans += 4*n*(n+1)//2
ans += 4*n
ans += 1

print(ans)
