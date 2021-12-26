
#我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。

#（这里，平面上两点之间的距离是欧几里德距离。）

#你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        tem = []
        for point in points:
            dis = point[0]**2 + point[1]**2
            tem.append(dis)
        #re = sorted(re,reverse=True)
        tem = sorted(range(len(tem)),key = lambda k : tem[k])
        re = []
        for index in tem[0:k]:
            re.append(points[index])
        return re 