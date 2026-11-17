class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.res = 0
        visited = set()
        
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]
        
        def dfs(cell): # (i, j)
            i, j = cell

            if cell in visited: 
                return 

            visited.add(cell)

            for di, dj in directions: 
                ni = i + di
                nj = j + dj 

                if ni < 0 or ni >= len(grid):
                    continue 
                if nj < 0 or nj >= len(grid[0]):
                    continue 
                
                if grid[ni][nj] == '1': 
                    dfs((ni, nj)) 
            return 
                

        for i in range(len(grid)): #rows 
            for j in range(len(grid[0])): #columns 
                if grid[i][j] == "1" and (i, j) not in visited: 
                    self.res += 1
                    dfs((i, j))
        return self.res
                
