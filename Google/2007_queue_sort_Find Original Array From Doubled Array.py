class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2 == 1:
            return []
        #先从小到大排序数组。设置 x*2 = y，那么y一定在x的后面
        changed = sorted(changed)
        re = []
        #队列先进先出
        queue = []
        #将小的那个入队，当遇到该值的二倍值时，将原值加入结果数组中
        #最终如果队列不为空，说明存在剩余无法匹配的数据，返回[]
        for index,value in enumerate(changed):
            if queue and queue[0] * 2 == value:
                re.append(queue[0])
                queue.pop(0)
            else:
                queue.append(value)
        if len(queue) != 0:
            return []
        else:
            return re 