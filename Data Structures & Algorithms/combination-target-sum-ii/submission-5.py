class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()
        n = len(candidates)
        
        def dfs(i):
            if sum(subset) == target and subset not in res:
                res.append(subset.copy())
                return 
            
            if i == n or sum(subset) > target:
                return 

            subset.append(candidates[i])
            dfs(i + 1)

            subset.pop()
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1)
        dfs(0)
        return res