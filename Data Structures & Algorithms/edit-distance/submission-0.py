class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {} # (i, j) --> min number of ops to make word1 == word2
        
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            if i == len(word1):
                return len(word2) - j # insertion operations 
            
            if j == len(word2):
                return len(word1) - i # deletion operations

            # if match
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]

            dp[(i, j)] = 1 + min(dfs(i + 1, j + 1), dfs(i + 1, j), dfs(i, j + 1))

            return dp[(i, j)]            

        return dfs(0, 0)