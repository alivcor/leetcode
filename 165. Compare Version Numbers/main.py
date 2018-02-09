def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    ver1 = version1.split(".")
    ver2 = version2.split(".")
    lv1 = len(ver1)
    lv2 = len(ver2)
    for i in xrange(max(lv1, lv2)):
        v1i = 0 if i >= lv1 else int(ver1[i])
        v2i = 0 if i >= lv2 else int(ver2[i])

        if (v1i > v2i):
            return 1
        elif v1i < v2i:
            return -1
        else:
            # both level version numbers are equal
            pass
    return 0