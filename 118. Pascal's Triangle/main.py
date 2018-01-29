def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """

    pascal_tr = []
    for x in xrange(numRows):
        pascal_tr.append([0]*(x+1))
    pascal_tr[0][0] = 1

    for i in xrange(1, numRows):
        lenr = len(pascal_tr[i])
        pascal_tr[i][0] = pascal_tr[i-1][0]
        pascal_tr[i][lenr-1] = pascal_tr[i-1][lenr-2]
        # printp(pascal_tr)
        for j in xrange(1, lenr-1):
            # print i,j
            pascal_tr[i][j] = pascal_tr[i-1][j] +pascal_tr[i-1][j-1]
    return pascal_tr

def printp(pt):
    for x in pt:
        print x

pt = generate(0)
printp(pt)