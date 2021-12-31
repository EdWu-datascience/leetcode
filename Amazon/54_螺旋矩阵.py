class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        mark = []
        for i in range(len(matrix)):
            mark.append([0]*len(matrix[0]))
        R = len(matrix)
        C = len(matrix[0])
        size = R*C 
        re = []
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        r = 0
        c = 0
        count = 0
        for i in range(size):
            re.append(matrix[r][c])
            mark[r][c] = 1
            direc = direction[count]
            r = r + direc[1]
            c = c + direc[0]
            if count >= 4:
                count = count%4
            #下面进行判断是否进行旋转,如果选择进行count + 1操作
            if r == R:
                r = r - direc[1]
                c = c - direc[0]
                count = (count+1)%4
                direc = direction[count]
                r = r + direc[1]
                c = c + direc[0]
            elif c == C:
                r = r - direc[1]
                c = c - direc[0]
                count = (count+1)%4 
                direc = direction[count]
                r = r + direc[1]
                c = c + direc[0]
            elif mark[r][c] == 1:
                r = r - direc[1]
                c = c - direc[0]
                count = (count+1)%4
                direc = direction[count]
                r = r + direc[1]
                c = c + direc[0]
        print(re)
        return re 