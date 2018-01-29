def strStr(haystack, needle):
    h = len(haystack)
    n = len(needle)
    if n == 0: return 0
    for i in xrange(h-n+1):
        for j in xrange(n):
            print "compare", haystack[i+j], needle[j]
            if haystack[i+j] != needle[j]: break
            if j == n-1: return i
    return -1


print strStr("aaa", "")