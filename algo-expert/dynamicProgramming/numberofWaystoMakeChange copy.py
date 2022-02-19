# O (nd) time | O (n) time

def minNumberOfWaystoMakeChange(n, denoms):
    numOfCoins = [float("inf") for amount in range( n+1)]
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in range(len(numOfCoins)):
            if denom <= amount:
                numOfCoins[amount] = min(numOfCoins[amount],
                numOfCoins[amount -denom] +1 )
    return numOfCoins[n] if numOfCoins[n] != float("inf") else -1



print(minNumberOfWaystoMakeChange(5,[1,2,3]))