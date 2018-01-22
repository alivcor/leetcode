def hasAlternatingBits(n):
    """
    :type n: int
    :rtype: bool
    """
    m = bin(n)
    return not any([m[i] == m[i+1] for i in range(len(m)-1)])

print hasAlternatingBits(4)