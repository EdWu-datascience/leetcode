class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #回溯法（探索与回溯法）是一种选优搜索法，又称为试探法，按选优条件向前搜索，
        #以达到目标。但当探索到某一步时，发现原先选择并不优或达不到目标，就退回一步重新选择，
        #这种走不通就退回再走的技术为回溯法，而满足回溯条件的某个状态的点称为“回溯点”。
        R = len(board)#number of rows
        C = len(board[0])#number of columns
        mark = []
        for i in range(R):
            mark.append([0]*C)
        def backtrack(i,j,board,mark,word):
            if len(word) == 0:
                return True
            for m,n in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                
                if m >=0 and m <= len(board)-1 and n >= 0 and n <= len(board[0])-1 and board[m][n] == word[0]:
                    if mark[m][n] == 1:
                        continue
                    mark[m][n] = 1
                    if backtrack(m,n,board,mark,word[1:]) == True:
                        return True
                    else:
                        mark[m][n] = 0

        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0]:
                    mark[i][j] = 1
                    if backtrack(i,j,board,mark,word[1:]) == True:
                        return True
                    else:
                        mark[i][j] = 0
        return False