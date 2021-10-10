#题目：
#给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

#数组中的每个元素代表你在该位置可以跳跃的最大长度。

#判断你是否能够到达最后一个下标。
#比如nums = [3,2,1,0,4]无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。return false

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #判断前一次可以跳的范围是否包含末端点，
        #倒数第二次的跳跃范围是否包含倒数第一次的点。
        #如果所有元素都不为0， 那么一定可以跳到最后；
        #从后往前遍历，如果遇到nums[i] = 0，就找i前面的元素j，使得nums[j] > i - j。
        #如果找不到，则不可能跳跃到num[i+1]，返回false。
        if 0 not in nums:
            return True
        if len(nums)==1:
            return True
        n = len(nums)-2
        flag = 0 
        while n >= 0:
            if nums[n] == 0:
                for i in range(0,n):
                    if nums[i] + i > n:
                        flag = 1 
                        break 
                if flag == 0:
                    return False
                flag = 0 
                n -= 1
            else:
                n -= 1
        return True  