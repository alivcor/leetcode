def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if (x < 0):
        y = -1 * int((str(x)[1:])[::-1])
    else:
        y = int(str(x)[::-1])
    if (abs(y) > (2 ** 31 - 1)):
        return 0
    else:
        return y


print reverse(1022)