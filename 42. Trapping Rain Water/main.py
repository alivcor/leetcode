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
        count += min(maxLeft, maxRight) - curr
    return count


def trapDP(heights):
    count = 0
    lenh = len(heights)
    if lenh == 0:
        return 0
    maxLeft = dict()
    maxRight = dict()
    maxLeft[0] = heights[0]
    maxRight[lenh - 1] = heights[lenh - 1]
    for x in xrange(1, lenh - 1):
        maxLeft[x] = max(maxLeft[x - 1], heights[x])
    for x in xrange(lenh - 2, 0, -1):
        maxRight[x] = max(maxRight[x + 1], heights[x])
    for x in xrange(1, lenh - 1):
        count += min(maxLeft[x], maxRight[x]) - heights[x]
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
randcase = [random.randint(1, maxHeight) for x in xrange(40)]

skyline(randcase, maxHeight)

print trap(randcase)
print trapOptimized(randcase)
print trapDP(randcase)