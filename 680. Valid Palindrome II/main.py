def validPalindrome_slow(s):
    """
    :type s: str
    :rtype: bool
    """
    if (s == s[::-1]): return True
    for i in xrange(len(s)):
        r = s[0:i] + s[i + 1:]
        if (r == r[::-1]): return True
    return False


def validPalindrome(s):
    def ispalin(i,j):
        return all(s[k]==s[j-k+i] for k in range(i,j))

    for i in xrange(0,len(s)/2):
        if(s[i] != s[len(s)-1-i]):
            j = len(s)-1-i
            return ispalin(i+1,j) or ispalin(i,j-1)
    return True

print validPalindrome("acbdvbca")