class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited, cycle = set(), set()
        
        preMap = {i: [] for i in range(numCourses)}

        for pre, crs in prerequisites: 
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in cycle: 
                return False
            
            if crs in visited:
                return True 
            
            if preMap[crs] == []:
                return True 
            
            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False 
            cycle.remove(crs)
            visited.add(crs)
            return True 

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True 