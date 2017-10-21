def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    else:
        s = str(x)
    lens = len(s)
    if any(s[i] != s[lens - i - 1] for i in xrange(lens)):
        return False
    return True

print isPalindrome(323892)