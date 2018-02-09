def reverseBits(n):
    res = 0
    for _ in xrange(32):
        res = res << 1
        if n&1 == 1:
            res = res + 1
        n = n >> 1
    return res

n = 13
print(bin(13))
print(bin(reverseBits(13)))
