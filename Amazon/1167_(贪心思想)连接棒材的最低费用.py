class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        #贪心思想，每次取最短的那两个
        sticks = sorted(sticks)   
        print(sticks) 
        if len(sticks) == 1:
            return 0
        re = 0
        while len(sticks) != 1:
            value = sticks[0] + sticks[1]
            re += value 
            sticks.append(value)
            sticks = sticks[2:]
            sticks = sorted(sticks)
        return re 