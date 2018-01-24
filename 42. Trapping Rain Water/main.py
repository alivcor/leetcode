
def trap(heights):
    """
    :type height: List[int]
    :rtype: int
    """
    count = 0
    lenh = len(heights)
    for x in xrange(lenh):
        curr = heights[x]
        maxLeft = max(heights[0:x]) if x != 0 else 0
        maxRight = max(heights[x+1:]) if x != lenh-1 else 0

        canhold = min(maxLeft, maxRight) - curr
        print canhold,
        if canhold > 0:
            count += canhold
    return count

def trapOptimized(heights):
    """
    :type height: List[int]
    :rtype: int
    """
    print heights
    count = 0
    lenh = len(heights)
    maxLeft = 0
    mli = 0
    maxRight = 0
    mri = lenh
    for x in xrange(lenh):
        print x, " | ",
        curr = heights[x]
        print "Current height is", curr, " | ",
        maxLeft = max(maxLeft, max(heights[mli:x])) if mli < x else 0
        print "maxLeft is ", maxLeft, " | ",
        mli = heights[mli:x].index(maxLeft) + x if mli < x else 0
        print "mli is ", mli, " | ",
        maxRight = max(maxRight, max(heights[x + 1:mri])) if x+1 < mri else 0
        print "maxRight is ", maxRight, " | ",
        mri = heights[x + 1:mri].index(maxRight) + x if x+1 < mri else lenh
        print "mri is ", mri, " | ",
        canhold = min(maxLeft, maxRight) - curr
        print canhold
        if canhold > 0:
            count += canhold
    return count



print trap([0,1,0,2,1,0,1,3,2,1,2,1])
print trapOptimized([0,1,0,2,1,0,1,3,2,1,2,1])