from time import time

def climbStairsBruteForce(s, n):
    if(s > n):
        return 0
    if(s == n):
        return 1
    return climbStairsBruteForce(s+1, n) + climbStairsBruteForce(s+2, n)


def climbStairsRecursionWithMemory(s, n, mem):
    if(s > n):
        return 0
    if(s == n):
        return 1
    try:
        if mem[s]:
            return mem[s]
    except KeyError:
        mem[s] = climbStairsRecursionWithMemory(s+1, n, mem) + climbStairsRecursionWithMemory(s+2, n, mem)
        return mem[s]

def climbStairsDPDict(n):
    if(n==1):
        return 1
    dp = dict()
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


def climbStairsDPList(n):
    if(n==1):
        return 1
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


def climbStairs(n, method):
    """
    :type n: int
    :rtype: int
    """
    if method == 1:
        return climbStairsBruteForce(0, n)
    if method == 2:
        mem = dict()
        return climbStairsRecursionWithMemory(0, n, mem)
    if method == 3:
        return climbStairsDPList(n)
    if method == 4:
        return climbStairsDPDict(n)




n = 12
start = time()
print climbStairs(n, 1), " | ",
print time() - start

start = time()
print climbStairs(n, 2), " | ",
print time() - start

start = time()
print climbStairs(n, 3), " | ",
print time() - start


start = time()
print climbStairs(n, 4), " | ",
print time() - start
