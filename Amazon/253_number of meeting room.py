class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #上下车问题
        #计算车上最多有几个人，该值则为需要的房间数量
        #分离出上车时间和下车时间
        up = []
        down = []
        for value in intervals:
            up.append([value[0],'up'])
            down.append([value[1],'down'])
        print(up)
        print(down)
        timeline = up + down
        timeline = sorted(timeline, key=(lambda x:(x[0],x[1])))
        print(timeline)
        count= [0]
        for value in timeline:
            if value[1] == 'up':
                count.append( count[-1]+1 )
            elif value[1] == 'down':
                count.append( count[-1]-1 )
        return max(count)