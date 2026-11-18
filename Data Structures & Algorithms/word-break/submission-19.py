class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        n = len(s)

        def dfs(i):
            if i == n:
                return True 

            if i in dp:
                return dp[i]

            for word in wordDict:
                if s[i:].startswith(word):
                    if dfs(i + len(word)): 
                        dp[i] = True
                        return dp[i]
            dp[i] = False
            return dp[i]

        return dfs(0)