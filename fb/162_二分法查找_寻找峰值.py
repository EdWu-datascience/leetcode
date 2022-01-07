class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #nums = [6,5,4,3,2,3,2]
        #nums = [3,1,2]
        #因为时间复杂度为O(logN),所以不能直接用max()函数得出结果，因为函数的时间复杂度为O(logN)
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        R = len(nums) - 1 
        L = 0
        #用二分法查找，查找大的那一半
        while L <= R:
            m = int( (R+L)/2 )
            if m == 0:
                if nums[m] > nums[m+1]:
                    return m
            elif m == len(nums) - 1:
                if nums[m] > nums[m-1]:
                    return m 
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m
            elif nums[m] < nums[m+1]:
                L = m+1
            elif nums[m] < nums[m-1]:
                R = m-1