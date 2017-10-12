
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

# grid = [[0,0,0,0,0,0,0,0]]
island_grid = grid

def maxAreaOfIsland(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    seen = set()
    def area(r, c):
        if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid) or grid[r][c] == 0 or (r,c) in seen):
            return 0
        seen.add((r, c))
        return 1 + area(r + 1, c) + area(r - 1, c) + area(r, c + 1) + area(r, c - 1)


    for r in range(len(grid)):
        for c in range(len(grid[0])):
            island_grid[r][c] = area(r,c)

    return max([max(x) for x in island_grid])

print maxAreaOfIsland(grid)


