def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    rev_s = []
    buffer_s = ""
    space_chain_flag = False
    for x in s:
        if x != " ":
            buffer_s = buffer_s + x
            space_chain_flag = False
        elif space_chain_flag == True and x == " ":
            pass
        else:
            rev_s.append(buffer_s)
            buffer_s = ""
            space_chain_flag = True
    # print rev_s
    rev_s.append(buffer_s)

    return (" ".join(str(x) for x in rev_s[::-1])).strip()

def reverseWordsPythonic(s):
    return " ".join(reversed(s.split())).strip()
    # print rev_s[::-1]

print reverseWords("sky is blue")
print reverseWords("   a   b ")
print reverseWordsPythonic("   a   b ")