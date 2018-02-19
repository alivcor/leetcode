def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if matrix == []: return False
    nr = len(matrix)
    nc = len(matrix[0])
    r = nr - 1
    c = 0
    while(r < nr and c < nc and r >= 0 and c >= 0):
        # print r, c, matrix[r][c]
        if(matrix[r][c] == target):
            return True
        elif(matrix[r][c] < target):
            c+=1
        else:
            r-=1
    return False


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 16
matrix = [[-5]]
target = -10

print(searchMatrix(matrix, target))