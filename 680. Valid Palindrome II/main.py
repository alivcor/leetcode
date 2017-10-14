def validPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    if (s == s[::-1]): return True
    for i in xrange(len(s)):
        r = s[0:i] + s[i + 1:]
        if (r == r[::-1]): return True
    return False

print validPalindrome("acbdvbca")