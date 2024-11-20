from functools import total_ordering


def coinChange(totalNumber,coins):
    N=totalNumber
    coins.sort()
    index=len(coins)-1
    while True:
        coinValue=coins[index]
        if N>= coins[index]:
            print(coinValue)
            N=N-coinValue
        if N<coinValue:
            index-=1
        if N==0:
            break

coins=[1,2,5,10,20,50,100,1000]
totalNumber=2035
coinChange(2035,coins)

