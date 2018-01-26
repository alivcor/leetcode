import random

def generateMatrix(S):
    return [[random.randint(1,10) for j in xrange(S)] for i in xrange(S)]


def printMatrix(m):
    for a in m:
        for b in a:
            print b,
        print ""
    print ""


def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    matrix.reverse()
    for i in xrange(len(matrix)):
        for j in xrange(i+1, len(matrix)): ##imp i+1
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp






testcase = [[1,2,3], [4,5,6], [7,8,9]]

m = generateMatrix(3)
m = testcase
printMatrix(m)
rotate(m)
printMatrix(m)
