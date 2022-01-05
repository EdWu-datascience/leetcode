
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #下列方法超出时间限制,时间复杂度：O(N**2)
        #前缀和思想
        nums = [1,-1,0]
        k = 0
        presum = []
        for index,value in enumerate(nums):
            presum.append(sum(nums[:index]))
        presum.append(sum(nums))
        #print(presum)
        #如果我们要获得nums[i] 到nums[j] (包含nums[i]和nums[j]) 区间的和
        #直接用presum[j+1] - presum[i]来表示
        re = []
        cnt = 0
        print(presum)
      
        
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                re.append(presum[j+1]-presum[i])
                if presum[j+1]-presum[i] == k:
                    cnt += 1
        
        print(re)
        return cnt 
