# O (nd) time | O (n) time

def numberOfWaystoMakeChange(n, denoms):
    ways = [0 for amount in range( n+1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount -denom]
    return ways[n]



print(numberOfWaystoMakeChange(5,[1,2,3]))