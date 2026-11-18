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

            dp[amt] = float('inf')
            for coin in coins:
                dp[amt] = min(1 + dfs(amt - coin), dp[amt])
            return dp[amt]
            
        result = dfs(amount)
        return -1 if result == float('inf') else dfs(amount)