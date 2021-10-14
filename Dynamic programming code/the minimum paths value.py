

#question:
#find a path that have the minimum value in the route,
#u can only move down or right each step
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        print(grid)
        path = []
        # m represent number of rows
        m = len(grid)
        # n represent number of columns
        n = len(grid[0])
        for i in range(m):
            path.append([0]*n)
        print(path)
        #(i,j) represent the sum of number to this point
        #central idea of this code
        #(i,j) = min(  [(i-1,j) + value on (i,j)] or [(i,j-1) + value on (i,j)]  )
        path[0][0] = grid[0][0]
        if m - 1 >= 1:
            path[1][0] = grid[1][0] + grid[0][0]
        if n - 1 >= 1:
            path[0][1] = grid[0][1] + grid[0][0]
        for M in range(m):

            for N in range(n):
                if (M == 0 and N == 0) or (M == 1 and N == 0) or (M == 0 and N == 1):
                    continue
                elif M == 0 and N != 0:
                    path[0][N] = path[0][N-1] + grid[M][N]
                elif M != 0 and N == 0:
                    path[M][0] = path[M-1][0] + grid[M][N]
                else:
                    path[M][N] = min(path[M-1][N]+grid[M][N],path[M][N-1]+grid[M][N])
        print(path)
        return path[-1][-1]
