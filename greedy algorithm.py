
#problem:
#Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
#The replacement must be in place and use only constant extra memory.





class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #nums = [2,6,3,5,4,1]
        #nums = [3,2,4,7,3]
        #nums=[3,2,1]
        #nums = [1,2,3]
        num = ''
        num_sort = ''
        #nums_sorted return the sorted list in descending order 
        nums_sort = sorted(nums,reverse=True)
        for i in range(0,len(nums)):
            num = num + str(nums[i])#num is str type of nums
            num_sort = num_sort + str(nums_sort[i])#num_sort is num in descending order 
        #if current order is already maxmimum, return list in ascending order
        flag = 0
        if num == num_sort:
            #nums = nums[::-1]
            #print('a')
            print(sorted(nums))
            #return nums
            flag = 1
        L = len(nums)-1
        
        for i in range(0,len(nums)):
            if flag == 1:
                break 
            num = nums[L-i]
            for j in range(0,L-i):
                #if left side of value less than right side, change the value, 
                #and sort the value after position L-i-j in ascending order 
                if nums[L-i-j-1] < num:
                    nums[L-i] = nums[L-i-1-j]
                    nums[L-i-1-j] = num 
                    right = sorted(nums[L-i-j:])
                    left = nums[0:L-i-j]
                    nums = left + right 
                    print(nums)
                    flag = 1
                    break
                    #return nums 
            if flag == 1:
                break 
                