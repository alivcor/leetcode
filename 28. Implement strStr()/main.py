def strStr(haystack, needle):
    for i in xrange(len(haystack)):
        for j in xrange(len(needle)):
            if j == len(needle)-1: return i
            if needle[j] != haystack[i+j]: return -1





print strStr("magazine", "zi")