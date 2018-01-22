def reverseWords(str):
    str1 = str.split(" ")
    str2 = []
    for word in str1:
        wdsplit = list(word)
        wdsplit = reversed(wdsplit)
        print wdsplit
        str2.append("".join(wdsplit))
    str2 = " ".join(str2)
    return str2

reverseWords("Abhinandan Dubey")