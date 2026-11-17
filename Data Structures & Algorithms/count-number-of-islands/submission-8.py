class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() # (i, j)
        self.res = 0
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        def dfs(i, j):

            if (i, j) in visited:
                return 
                
            visited.add((i, j))

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if ni < 0 or ni >= len(grid):
                    continue
                
                if nj < 0 or nj >= len(grid[0]):
                    continue 

                if grid[ni][nj] == "1": 
                    dfs(ni, nj)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited: 
                    self.res += 1
                    dfs(i, j)

        return self.res



        
