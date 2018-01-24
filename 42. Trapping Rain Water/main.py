

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
        # print canhold
        if canhold > 0:
            count += canhold
    return count



print trap([0,1,0,2,1,0,1,3,2,1,2,1])