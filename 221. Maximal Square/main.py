
def maximalSquareDoesntWork(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix: return 0
    maxL = min(len(matrix), len(matrix[0]))
    areas_of_interest = []
    for row in matrix:
        print row
        cnt = 0
        chunk_was_set = False
        for i in xrange(len(row)):
            val = row[i]
            if val == 1:
                cnt += 1
            else:
                if cnt > 0:
                    chunk = [i - cnt, cnt]
                    cnt = 0
                    chunk_was_set = True
            print "i =", i, "val =", val, "cnt =", cnt
        if cnt > 0:
            if chunk_was_set:
                # compare current with originally in larg
                if chunk[1] < cnt:
                    chunk = [i - cnt + 1, cnt]
            else:
                chunk = [i - cnt + 1, cnt]
        print "larg :", chunk
        print ""
        areas_of_interest.append(chunk)
    print areas_of_interest

    len_longest_decr_seq = 0
    cnt = 0
    for i in xrange(1, len(areas_of_interest)):
        j = i - 1
        if areas_of_interest[i][0] <= areas_of_interest[j][0] and areas_of_interest[i][1]:
            cnt +=1
        else:
            if cnt > 0:
                pass
    return chunk


def maximalSquare(matrix):
    S = [[0 for _ in xrange(len(matrix[0]))]]*len(matrix)

    print S



matrix = [[1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0]]

print maximalSquare(matrix)