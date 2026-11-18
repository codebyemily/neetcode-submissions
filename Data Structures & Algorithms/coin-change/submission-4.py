class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        res = 0

        def dfs(amt):
            if amt < 0:
                return float('inf')
                
            if amt == 0:
                return 0 # no more coins that can be added 
            
            if amt in dp:
                return dp[amt]

            res = float('inf')
            for coin in coins:
                res = min(1 + dfs(amt - coin), res)
            dp[amt] = res
            return dp[amt]
            
        res = dfs(amount)
        return -1 if res == float('inf') else dfs(amount)