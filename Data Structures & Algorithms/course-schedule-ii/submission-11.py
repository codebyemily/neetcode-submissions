class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        self.res = []

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        cycle = set()
        visited = set()

        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visited:
                return True 

            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            self.res.append(crs)
            cycle.remove(crs)
            visited.add(crs)
            return True 
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return self.res