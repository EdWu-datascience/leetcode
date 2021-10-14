
#question:
#same as how many different path,but in this quesition,we need to consider there is block on the grid,
#Q64





class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1 and obstacleGrid[0][0]==0:
            return 1 
        elif len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1 and obstacleGrid[0][0]==1:
            return 0
        print(obstacleGrid)
        # m represent number of rows
        m = len(obstacleGrid)
        # n represent number of columns
        n = len(obstacleGrid[0])
        path = []
        #initial path [0][0] and [1][0] and [0][1]
        for i in range(m):
            path.append([0]*n)
        if obstacleGrid[0][0] == 0:
            path[0][0] = 0
        else:
            path[0][0] = 0
        if m - 1 >= 1:
            if obstacleGrid[1][0] == 0 and obstacleGrid[0][0] == 0:
                path[1][0] = 1
            else:
                path[1][0] = 0
        if n - 1 >= 1:
            if obstacleGrid[0][1] == 0 and obstacleGrid[0][0] == 0:
                path[0][1] = 1
            else:
                path[0][1] = 0
                
                
        #(A,B) A represent number of path, B represent whether this path went 
        #through obstacle.
        print(path)
        for M in range(m):
            for N in range(n):
                if (M == 0 and N == 0) or (M == 1 and N == 0) or (M == 0 and N == 1):
                    continue
                else:
                #for the if and elif in the following code,the first represent M==0 and N != 0, what's the number of path to [M][N]
                #we need to consider this: because this is a straghtline,so the path should always <= 1, and if there is block from
                #[M][0:N+1] the number of path should be zero(note: consider [M][0:N+1] not [M][0:N] that's how i get it wrong in the            
                #first time)
                    if M == 0 and N != 0:
                        obstacle = 0
                        for i in obstacleGrid[0][0:N+1]:
                            if i == 1:
                                obstacle = 1
                        if obstacle == 1:
                            path[M][N] = 0
                        else:
                            path[M][N] = 1
                    elif M != 0 and N == 0:
                        obstacle = 0
                        for i in obstacleGrid[0:M+1]:
                            if i[0] == 1:
                                obstacle = 1
                        if obstacle == 1: 
                            path[M][N] = 0
                        else:
                            path[M][N] = 1
                    else:
                        value = path[M-1][N] + path[M][N-1]
                        obstacle = obstacleGrid[M][N]
                        if obstacle == 1:
                            path[M][N] = 0
                        else:
                            path[M][N] = value 
        print(path)
        print(path[m-1][n-1])
        return path[m-1][n-1]
