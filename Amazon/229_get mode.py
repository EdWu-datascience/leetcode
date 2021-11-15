#给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        n = len(nums)
        for i in range(0,len(nums)):
            if nums[i] not in count.keys():
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        re = []
        for key,value in count.items():
            if value > n/3:
                re.append(key)
        print(re)
        return re 