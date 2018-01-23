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



start = time()
print climbStairs(3, 1), " | ",
print time() - start

start = time()
print climbStairs(3, 2), " | ",
print time() - start
