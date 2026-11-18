from collections import deque 

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque() # [(i, j)]
        visited = set()

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        # initialize chests
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        while q: 
            i, j = q.popleft()

            if (i, j) in visited:
                continue
                
            for di, dj in directions: 
                ni = i + di
                nj = j + dj 

                # check bounds
                if ni < 0 or ni >= len(grid):
                    continue
                if nj < 0 or nj >= len(grid[0]):
                    continue

                if (ni, nj) not in visited and grid[ni][nj] == 2147483647:
                    q.append((ni, nj))
                    grid[ni][nj] = grid[i][j] + 1 
                    
