class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #先排序
        #intervals = [[2,6],[1,3],[8,10],[15,18]]
        intervals = sorted(intervals,key=(lambda x:x[0]))
       
        merge = [intervals[0]]
        for index,value in enumerate(intervals):
           
            if value[0] > merge[-1][1]:
                merge.append(value)
            else:
                merge[-1][1] = max(merge[-1][1],value[1])
        print(merge)
        return merge