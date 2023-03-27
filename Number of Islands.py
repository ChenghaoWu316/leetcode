
class Solution:
    def __init__ (self):
        self.root = {}
        self.count = 0

    def find(self, x):
        if self.root[x] == -1:           
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        RootX = self.find(x)
        RootY = self.find(y)
        if RootX != RootY:
            self.root[RootY] = RootX
            self.count -=1

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    self.root[row*cols + col] = -1
                    self.count +=1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    #scan locations for 4 directions using tuple
                    for (r,c) in [(1,0),(0,1),(-1,0),(0,-1)]:
                        newrow = row + r
                        newcolumn = col + c
                        if  0 <= newrow <= rows-1 and 0 <= newcolumn <= cols-1 and grid[newrow][newcolumn] == "1":
                            self.union(row*cols+col , newrow*cols + newcolumn)
        return self.count
