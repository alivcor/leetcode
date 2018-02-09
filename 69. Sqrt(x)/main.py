def sqrt2(x):
    if x == 0: return 0
    left = 1
    right = x
    while(left<=right):
        mid = left + (right-left)/2
        if mid == x/mid:
            return mid
        if(mid < x/mid):
            left = mid + 1
        else:
            right = mid - 1
    return right


print sqrt2(23)