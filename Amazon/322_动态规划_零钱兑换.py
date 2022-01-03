class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #coins = [2]
        #amount = 3 
        if amount == 0:
            return 0
        elif min(coins) > amount:
            return - 1
        dp = [2**31]*(amount+1)
        dp[0] = 0
        #用动态规划
        #dp[i]用来存储到达总金额i所需要的最少硬币数
        #状态转移方程：
        #dp[i] = min( dp[i-coins[j]] ) + 1 这里j从0取到len(coins)
        for i in range(1,amount+1):
            temp = []
            for j in range(len(coins)):
                if i - coins[j] < 0:
                    continue
                else:
                    temp.append(dp[i-coins[j]])
            if len(temp) != 0:
                dp[i] = min(temp)+1
        print(dp)
        if dp[-1] >= 2**31:
            return -1
        else:
            return dp[-1]