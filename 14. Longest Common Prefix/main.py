strs = ["addjs", "addidas", "addsad"]
if len(strs) == 0: print ""
lcp = ""
for i in xrange(min([len(x) for x in strs])):
    if (all(strs[j][i] == strs[j + 1][i] for j in xrange(len(strs) - 1))):
        lcp = lcp + strs[0][i]
    else:
        print lcp
        exit(0)
print lcp

