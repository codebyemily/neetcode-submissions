class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False 
        
        half = sum(nums) / 2
        n = len(nums) 
        
        dp = {} # (index, rem) --> True/False

        def dfs(i, rem):
            if i >= n:
                return False
            
            if rem == 0:
                return True 
            
            if (i, rem) in dp:
                return dp[(i, rem)]

            dp[(i, rem)] = dfs(i + 1, rem) or dfs(i + 1, rem - nums[i])
            return dp[(i, rem)]
        return dfs(0, half)

