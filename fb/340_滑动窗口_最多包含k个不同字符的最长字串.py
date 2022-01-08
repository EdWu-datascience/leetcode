class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        '''
        #先存储每个字符的频数
        freq = {}
        for value in s:
            if value not in freq.keys():
                freq[value] = 1
            else:
                freq[value] += 1 
        print(freq)
        '''
        '''
        #下列方法超出时间限制，时间复杂度为O(N**2)
        Max = 0
        for i in range(len(s)):

            for j in range(i,len(s)+1):
                if i == j:
                    continue
                #s[i:j]长度为
                length = len(s[i:j])
                quantity = len(set(list(s[i:j])))#包含的不同字符的数量
                if quantity <= k:
                    Max = max(Max,length)
        return Max 
        '''
        #使用滑动窗口
        #右边界一直右移，当字符串种类大于k时，有边界停止，左边界右移，直到字符串种类小于等于
        #k时，让右边界右移，右边界右移的结束是到字符串尾部，
        #整个终止条件是当左边界移动到字符串结尾
        if k == 0:
            return 0
        if len(s)== 1 and k >1:
            return 1
        if len(s) == 1 and k==1:
            return 1 
        elif len(s) == 1 and k==0:
            return 0
        left = 0
        right = 1
        Max = 0
        while left != len(s)-1:
            #print(left)
            sub = s[left:right]
            length = len(sub)
            quantity = len(set(list(sub)))
            if quantity <= k:
                Max = max(length,Max)
            if quantity <= k and right != len(s):
                right += 1
            else:
                left += 1 
        return Max