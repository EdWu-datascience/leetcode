class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #先找到每个字符的起始位置和终止位置
        place = {}
        for index,value in enumerate(s):
            if value not in place.keys():
                place[value] = [index]
            elif len(place[value]) == 1:
                place[value].append(index)
            else:
                place[value][-1] =  max(index, place[value][-1]) 
        #print(place)
        #首先从第一个字母开始，记录其起始位置和终止位置，然后比较在这个范围中
        #的其他字母的终止位置和该字母的终止位置的值，如果小于则不作为，如果大于则更新该状态
        #下的终止位置。
        start = place[s[0]][0]
        end = place[s[0]][-1]
        L = len(s)
        flag = 0
        re = []
        
        while end != L - 1:
            
            for index in range(start,end+1):
                if place[s[index]][-1] > end:
                    end = place[s[index]][-1]
                    flag = 1 #flag = 1 用来标记该轮循环end的位置发生了改变
            if flag == 0:   #flag 如果==0则说明此轮end的位置没有发生改变
                re.append(end-start+1)
                start = end + 1 
                end = place[s[start]][-1]
            flag = 0
        re.append(end-start+1)
        print(re)
        return re 
