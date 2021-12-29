class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #用dp[i]表示字符串s前i个字符s[0]~s[i-1]组成的字符串
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(0,i+1):
                if s[j:i] in wordDict and dp[j] == True:
                    dp[i] = True
        print(dp)
        return dp[-1]