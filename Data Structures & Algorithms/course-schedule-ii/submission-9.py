class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites: 
            preMap[crs].append(pre)

        visited = set()
        cycle = set()
        res = []

        def dfs(crs):
            if crs in cycle:
                return False 
            
            if crs in visited:
                return True 
            
            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                    
            res.append(crs)
            cycle.remove(crs)
            visited.add(crs)
            return True 

        # check every single course
        for crs in preMap: 
            if not dfs(crs):
                return []
        return res
        