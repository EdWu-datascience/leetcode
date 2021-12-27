class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #先判断是否存在腐烂的橘子：
        flag1 = 0   #flag1用来判断是否存在好橘子
        flag2 = 0   #flag2用来判断是否存在坏橘子
        for i in range(len(grid)):
            if 2 in  grid[i]:
                flag2 = 1 
            if 1  in grid[i]:
                flag1 = 1
        if flag1 == 0:  #先判断flag1的值再判断flag2的值
            return 0   
        if flag2 == 0:
            return -1 
        row = len(grid)
        col = len(grid[0])
        #遍历找到所有腐烂橘子的位置,作为起始层
        rot = []
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == 2:
                    rot.append([i,j,0]) #第三个值用来存储天数
        count = 0
        def neighbor(rn,cn):    #这个函数的作用是判断当前坏橘子上下左右是否超出边界
            temp = [[rn-1,cn],[rn+1,cn],[rn,cn-1],[rn,cn+1]]
            for r,c in temp:
                if 0 <= r <= row - 1 and 0 <= c <= col - 1:
                    yield r,c
                    #使用yield相当于把函数转变成了一个generator
        while rot:
            r,c,count = rot.pop(0)# rot队列遵循先进先出的原则
            for nr,nc in neighbor(r,c):
                #如果neighbor使用return的话会报错can't unpack non-iterate int object
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    rot.append([nr,nc,count+1])#同一层的坏橘子虽然不会同步在一个循环中执行，但是因为同一层的坏橘子坏的时间是相同的(初始值设置为了0),所以等效于同一天发生。
        for row in grid:
            if 1 in row:
                return -1
        return count