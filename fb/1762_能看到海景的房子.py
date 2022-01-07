class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        '''
        #下面的代码时间复杂度为O(N**2)
        re = []
        for index,value in enumerate(heights):
            if index == len(heights) - 1:
                break
            if value > max(heights[index+1:]):
                re.append(index)
        re.append(len(heights)-1)
        re = sorted(re)
        print(re)
        return re 
        '''
        #优化后的代码时间复杂度O(N)
        re = []
        Max = 0
        for index in range(1,len(heights)+1):
            if heights[-index] > Max:
                re.append(len(heights)-index)
                Max = heights[-index]
            #print(len(heights)-index)
            #print(heights[-index])
        print(re)
        return sorted(re)