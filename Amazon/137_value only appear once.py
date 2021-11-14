
#137
#给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        n = len(nums)
        for i in range(0,n):
            if nums[i] not in count.keys():
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        for key,value in count.items():
            if value == 1:
                return key