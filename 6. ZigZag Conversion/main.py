s = "ABCDE"
n = 4
r = ""
if n == 1:
    print s
else:
    big_step = 2*(n-1)
    for i in range(n):
        if i == 0 or i == n-1:
            for j in range(i, len(s), big_step):
                r = r + s[j]
                print r
        else:
            isPillar = False # first step you'll take is into the slough, you always start at first column which is a pillar.
            j = i
            # big_step = slough_step + pillar_step
            slough_step = big_step - 2*i
            pillar_step = big_step - slough_step
            while(j < len(s)):
                print i, j, r
                r = r + s[j]
                if(isPillar):
                    j = j + pillar_step
                    isPillar = False
                else:
                    j = j + slough_step
                    isPillar = True
    print r



