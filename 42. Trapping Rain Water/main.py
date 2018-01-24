import random

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
        # print canhold,
        if canhold > 0:
            count += canhold
    return count

def trapOptimized(heights):
    """
    :type height: List[int]
    :rtype: int
    """
    count = 0
    lenh = len(heights)
    for x in xrange(1, lenh-1):
        maxLeft = maxRight = 0
        curr = heights[x]
        for i in xrange(0, x+1):
            maxLeft = max(maxLeft, heights[i])
        for j in xrange(x, lenh):
            maxRight = max(maxRight, heights[j])
        canhold = min(maxLeft, maxRight) - curr
        # print canhold,
        count += canhold

    return count


def skyline(heights, maxHeight):
    print heights
    print "\n"
    for n in xrange(maxHeight, 0, -1):
        for i in heights:
            # print n, i,
            if i >= n:
                print unichr(0x2588),
            else:
                print " ",
        print ""
    print "\n"



testcase = [0,1,0,2,1,0,1,3,2,1,2,1]
maxHeight = 6
randcase = [random.randint(0, maxHeight) for x in xrange(10)]

skyline(randcase, maxHeight)

print trap(randcase)
print trapOptimized(randcase)