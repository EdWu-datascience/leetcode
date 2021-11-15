#给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

#子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[i]代表到i最长的严格递增子序列的长度
        #对于j属于[0,i)的，当nums[j] < nums[i] 时，nums[i]可以接在nums[j]之后，
        #此情况下长度上升到dp[j] + 1

        dp = [1]*len(nums)#设置dp每个位置的初始值为1是因为每个值都可以单独成为一个最长
        #严格递增子序列        
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    #dp[j] += 1
                    dp[i] = max(dp[i],dp[j]+1)
        print(dp)
        return max(dp)