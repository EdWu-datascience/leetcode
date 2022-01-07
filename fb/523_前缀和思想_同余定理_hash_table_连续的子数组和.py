class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        #下列方法超出时间限制，时间复杂度O(N**2)，需要优化
        #前缀和思想
        #nums长度大于等于1
        if len(nums) < 2:
            return False
        pre = []
        for i in range(len(nums)+1):

            for j in range(i,len(nums)+1):
                if i == j:
                    continue
                if len(nums[i:j]) >= 2: 
                    pre.append(nums[i:j])
        print(pre)
        for value in pre:
            S = sum(value)
            if S % k == 0:
                return True
        return False
        '''
        #优化
        #利用同余定理：如果两个整数a-b能够被c整除，那么就称a和b对c同余，即a%c == b%c
        #前缀和思想，
        #presum[i] 表示nums数组下标0到下标i的前缀和
        #nums区间i到j(包含下标为i和j的value)和为presum[j+1] - presum[i],该区间的长度为j-i+1
        if len(nums) < 2:
            return False
        '''
        presum = [[0]]
        for i in range(1,len(nums)+1):
            presum.append(nums[:i])
        
        for index in range(len(presum)):#这个的时间复杂度为O(N**2)
            presum[index] = sum(presum[index])
        '''
        #优化上面的两个for循环代码
        presum = [0]*(len(nums)+1)
        for i in range(0,len(nums)):
            presum[i+1] = nums[i] + presum[i]
        print(presum)
        hash_table = {}
        #hash_table中只记录每个余数第一次出现的index，如果当前的余数存在于hash表中
        #比较当前的index和table已经存在的index,长度就是二者index差，如果>=2,返回true
        #否则返回false
        for index,value in enumerate(presum):
            #key 代表余数，value代表该余数第一次出现的位置
            value = presum[index]%k
            if value not in hash_table.keys():
                hash_table[value] = index
            else:
                if index - hash_table[value] >= 2:
                    return True 
        return False