
#只需要比较第一次跳跃的最远距离是否大于跳跃过程中遇到的点的最远距离。
#Q55
class Solution:
    def jump(self, nums: List[int]) -> int:
        #motherfucker 
        if len(nums) == 1:
            return 0
        count = 0
        flag = 0 
        c = 0
        #最大跳跃的距离,前者存储value，后者存储index
        maxdistance = [nums[0],0]
        while maxdistance[1] <= len(nums)-1:
            start = maxdistance[1]
            distance = maxdistance[0]
            if start + distance >= len(nums)-1:
                count += 1 
                print(count)
                return count 
            else:
                #查看这个过程中是否存在可以跳的更远的点，如果存在则修改start和distance的值
                for j in range(start+1,start+distance+1):
                    if start + distance <= nums[j]+j:
                        flag = 1 
                        start = j
                        distance = nums[j]
                if flag == 0:
                    maxdistance[1] = start + distance 
                    maxdistance[0] = nums[start+distance]
                else:
                    maxdistance[1] = start
                    maxdistance[0] = distance
                count += 1 
