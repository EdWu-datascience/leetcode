class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #这个是岛屿问题,深度优先遍历
        #深度优先遍历不是向四个方向，而是一条线走到底
        def DFS(isConnected,i):
            for j in range(col):
                if isConnected[i][j] == 1:
                    isConnected[i][j] = 0#将访问过的节点改为0
                    DFS(isConnected,j) 


            
            
        cnt = 0
        row = len(isConnected)
        col = len(isConnected[0])
        for i in range(len(isConnected)):

            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    DFS(isConnected,i)
                    cnt += 1 
        return cnt 