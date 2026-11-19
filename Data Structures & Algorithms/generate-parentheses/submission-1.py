class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = ""
        
        def backtrack(subset, left, right):
            if n * 2 == len(subset):
                res.append(subset)
                return 
            

            if left < n:
                backtrack(subset + "(", left + 1, right)
            if right < left: 
                backtrack(subset + ")", left, right + 1)
        backtrack(subset, 0, 0)
        return res