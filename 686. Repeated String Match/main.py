def repeatedStringMatch(A, B):
    """
    :type A: str
    :type B: str
    :rtype: int
    """
    q = len(B)/len(A)
    if B in A*q: return q
    if B in A*(q+1): return q+1
    return -1


print repeatedStringMatch("abcd", "cdabcdab")