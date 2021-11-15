
#给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(0,len(nums)):
            key = nums[i]
            if key not in count.keys():
                count[key] = 1
            else:
                count[key] += 1
        a = sorted(count.items(), key = lambda item:item[1])
        re = []
        for i in range(1,k+1):
            re.append(a[-i][0])
        return re 