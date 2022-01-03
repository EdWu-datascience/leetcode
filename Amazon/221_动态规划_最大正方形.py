class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #动态规划：
        #dp[i][j]表示以[i][j]为右下角，且只包含1的正方形的边长最大值
        #如果该位置的值为零，则dp[i][j] = 0
        #如果该位置的值为一，则dp[i][j]的值由其上方，左方和左上角三个值决定
        #状态转移方程如下：
        #dp[i][j] = min( dp[i-1][j],dp[i-1,j-1],dp[i][j-1] ) + 1
        row = len(matrix)
        col = len(matrix[0])
        #dp = [ [0]*col ]*row
        #不能使用上面dp初始化方法，貌似会导致指向同一个存储空间，比如取dp[0][2] == 1 
        #则会导致整个j==2的列值变成1
        dp = []
        maxside = 0
        for i in range(row):
            dp.append([0]*col)
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '0':                       
                    dp[i][j] = 0
                else:
                    #还要考虑边界条件
                    #i==0 和 j==0 单独拿出来，因为此时i-1<0，j-1 <0
                    #而且我们是将[i][j]作为正方形的右下角作为先决条件
                    #因此i==0或者j==0时的dp[i][j]只能是1或者0，即dp[i][j] = matrix[i][j]
                    if i == 0 or j == 0:
                        dp[i][j] = int(matrix[i][j])
                    else:
                        dp[i][j] = min( dp[i-1][j],dp[i-1][j-1],dp[i][j-1] )+1
                maxside = max(dp[i][j],maxside)
        print(dp)
        print(maxside)
        return maxside**2