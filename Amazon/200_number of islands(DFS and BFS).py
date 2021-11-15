

#给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

#岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

#此外，你可以假设该网格的四条边均被水包围。


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #bfs
        def bfs(grid,i,j):
            queue = [[i,j]]
            while queue:
                [i,j] = queue.pop(0)
                if 0 <= i < len(grid) and 0<= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue += [[i+1,j],[i-1,j],[i,j-1],[i,j+1]]
        count = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == '0' : continue
                bfs(grid,i,j)
                count += 1 
        return count 
        '''
        #Depth first search
        def DFS(grid,i,j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0': return
            grid[i][j] = '0'
            DFS(grid,i-1,j)
            DFS(grid,i+1,j)
            DFS(grid,i,j-1)
            DFS(grid,i,j+1)
        row = len(grid)
        column = len(grid[0])
        count = 0
        for i in range(0,row):
            for j in range(0,column):
                if grid[i][j] == '1':
                    DFS(grid,i,j)
                    count += 1
        return count  
        '''