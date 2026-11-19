class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        n = len(nums)
        
        def dfs(i):
            if sum(subset) == target and subset not in res:
                res.append(subset.copy())
            
            if i >= n or sum(subset) > target: 
                return 

            subset.append(nums[i])
            dfs(i)

            subset.pop()
            dfs(i + 1)
            
        dfs(0)
        return res 
