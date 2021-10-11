
#question:
#a robat located at a m×n grid, and the robat can only move the right or down for one step each time
#calculate how many paths do we have to get to the point (m-1,n-1)


#f(i,j)represent the number of paths to point(i,j),and we can have this equation: f(i,j)=f(i-1,j)+f(i,j-1)
#boundary condition:
#i-1 <0 when i == 0 and j-1 < 0 when j == 0
#so we need to put these point out of for loop. We also need to consider the value of m and n in case one of them == 1 
#so there will no (0,1) or (1,0)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = []
        for i in range(m):
            path.append([0]*n)
        print(path)
        #
        path[0][0] = 1
        if n-1 >= 1:
            path[0][1] = 1 
        if m-1 >= 1:
            path[1][0] = 1
            
        #   
        for M in range(0,m):
            for N in range(0,n):
                if (M == 0 and N == 0) or (M == 0 and N == 1) or (M == 1 and N == 0):
                    continue
                else:
                    path[M][N] = path[max(M-1,0)][N] + path[M][max(N-1,0)]
        print(path)
        return path[m-1][n-1]
