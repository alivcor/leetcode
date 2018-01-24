

def trap(heights):
    """
    :type height: List[int]
    :rtype: int
    """
    count = 0
    lenh = len(heights)
    maxLeft = 0
    mli = 0
    maxRight = 0
    mri = 0
    for x in xrange(lenh):
        curr = heights[x]
        maxLeft = max(heights[mli:x]) if mli < x else 0
        mli = heights.index(maxLeft)
        maxRight = max(heights[x + 1:mri]) if x+1 < mri else 0
        mri = heights.index(maxRight)
        canhold = min(maxLeft, maxRight) - curr
        print canhold
        if canhold > 0:
            count += canhold
    return count



print trap([0,1,0,2,1,0,1,3,2,1,2,1])