s = "abbabab"

argmax = 0
maxval = ""
for i in xrange(len(s)):
    for j in xrange(i, len(s)):
        print "i = " + str(i) + " | j = " + str(j),
        r = s[i:j+1]
        lenr = len(r)
        if lenr > argmax and r[0] == r[lenr-1]:
            if r == r[::-1]:
                #palin
                argmax = lenr
                maxval = r
        #     else:
        #         print "Skipping 2 - " + r
        # else:
        #     print "Skipping - 1 - " + r

print maxval, argmax
