#!/usr/bin/env python3

#In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#It is possible to make £2 in the following way:
#
#1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#How many different ways can £3 be made using any number of coins?

coins = [0,1,2,5,10,20,50,100,200]

def partition(amount,coin):
    next_smaller = coins[coins.index(coin)-1]
    if amount==coin:
        return 1+partition(amount,next_smaller)
    if coin==0 or amount<0:
        return 0
    if amount==0 or coin==1:
        return 1

    return partition(amount, next_smaller) + partition(amount-coin, coin)

print(partition(200, 200))
