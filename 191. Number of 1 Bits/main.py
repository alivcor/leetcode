def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """

    cnt = 0
    s = str(bin(n))[2:]
    for x in s:
        if x == '1':
            cnt+=1
    print "Hamming Weight of", n, "is", cnt


def hammingWeightFast(n):
    k = n
    cnt = 0
    while(n):
        n = n&(n-1)
        cnt+=1
    print "Hamming Weight of", k, "is", cnt

hammingWeight(122)
hammingWeightFast(122)