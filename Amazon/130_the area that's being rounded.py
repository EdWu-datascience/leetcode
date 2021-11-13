
#130
#给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

#被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，
#或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)# m is number of rows
        n = len(board[0])# n is number of columns
        for L in range(0,m):
            element = board[L]
            for j in range(0,len(element)):
                #先将边界的O 变成 B
                #first we change the value "O" at border to "B"  
                if (L == 0 or L == m - 1 or j == 0 or j == n - 1) and board[L][j] == 'O':
                    board[L][j] = 'B'
        
        #当循环没有变成#的时跳出while
        #this while loop is to change all of the value "O" that is connect with border
        # "B" to "#"
        while True:
            flag = 0
            for L in range(0,m):
                element = board[L]
                for j in range(0,len(element)):
                # 找到和边界联通的 O,并将其变成#应该是这一步有问题
                    if board[L][j] == 'O':
                        if board[L-1][j] == 'B' or board[L+1][j] == 'B' or board[L][j+1] =='B' or board[L][j-1] == 'B' or board[L-1][j] == '#' or board[L+1][j] == '#' or board[L][j+1] =='#' or board[L][j-1] == '#':
                            board[L][j] = '#'
                            flag = 1
            if flag == 0:
                break 
        #把B变成O
        #change B to O
        for L in range(0,m):
            element = board[L]
            for j in range(0,len(element)):
                if board[L][j] == 'B':
                    board[L][j] = 'O'
                elif board[L][j] == 'O':
                    board[L][j] = 'X'
        #change # to O
        for L in range(0,m):
            element = board[L]
            for j in range(0,len(element)):
                if board[L][j] == '#':
                    board[L][j] = 'O'
        print(board)