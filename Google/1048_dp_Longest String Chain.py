class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        #建立一个check函数判断word1是否是word2的predecessor
        #先sorted，因此会有word1长度小于等于word2长度，因此遍历word2
        def check(word1,word2):
            l1 = len(word1)
            l2 = len(word2)
            i,j = 0,0 
            if l1 + 1 != l2:#先判断word1和word2长度是否正好差了1
                return False
            while i < l1 and j < l2:
                if word1[i] == word2[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            return i == l1

        words = sorted(words,key = lambda x:len(x))
        #时间复杂度为O(N**2)
        #动态规划
        #对于第i个字符串，如果在[0, i-1]的范围内找到了某个长度减一的字符串，检查其能否组成链。
        #如果能，更新目前的最大长度。
        dp = [1]*len(words)
        re = 1
        for i in range(len(words)):
            cur = 1
            for j in range(i):

                if len(words[j]) + 1 == len(words[i]):
                    temp = check(words[j],words[i])   
                    if temp == True:
                        cur = max(cur,dp[j]+1)
            dp[i] = cur
            re = max(re,dp[i])
        return re 
