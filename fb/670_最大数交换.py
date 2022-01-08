
class Solution:
    def maximumSwap(self, num: int) -> int:
       # num = 1993  #预期结果9913
        #num = 9973
        #num = 98368 #预期结果：98863
        if len(str(num)) < 2:#如果num长度小于2的话不用交换直接返回值本身
            return num 
        nums1 = []
        for i in str(num):
            nums1.append(int(i))
        print(nums1)
        #思路，sort 从大到小排序原数，找到第一个和原数不同的地方的index1，然后找到该数值原来的位置   
        #index2(该数值可能在原来的数中重复出现，如果重复出现则找最大的那个index2)
        nums2 = sorted(nums1.copy(),reverse=True)
        print(nums2)
        #先记录每个value出现的index最大的地方
        position = {}
        for index,value in enumerate(nums1):
                position[value] = index
        print(position)
        
        for index2,value in enumerate(nums2):
            if value != nums1[index2]:
                #找到value 在nums1中的index
                index1 = position[value]
                temp = nums1[index2]
                nums1[index2] = nums1[index1]
                nums1[index1] = temp
                break 
        print(nums1)
        re = ''
        for value in nums1:
            re += str(value) 
        return int(re)