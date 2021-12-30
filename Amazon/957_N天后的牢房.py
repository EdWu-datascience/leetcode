class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:        
        n = n%14
        #要加上下面的if语句判断n是否等于0，如果等于0要将n设置为14
        if n == 0:
            n = 14
        for i in range(n):
            temp = cells.copy()
            for j in range(1,7):#cells的长度固定：8
                if cells[j-1] == 1 and cells[j+1] == 1:
                    temp[j] = 1
                elif cells[j-1] == 0 and cells[j+1] == 0:
                    temp[j] = 1
                else:
                    temp[j] = 0
            temp[0] = 0 #第一间和最后一间从第二天开始会一直保持着为0的状态
            temp[7] = 0            
            cells = temp
            '''
            #结果显示14天是一个周期
            if cells in re:
                re.append(cells)
                print(re)
                print(re.index(cells))
                break
            re.append(cells)
            '''     
        print(cells)
        return cells 