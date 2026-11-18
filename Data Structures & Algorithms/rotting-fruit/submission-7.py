class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque() # (i, j, m)
        fresh = 0
        visited = set() # (i, j)
        minutes = 0
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1 
        while q:
            i, j, m = q.popleft()

            if (i, j) in visited: 
                continue 
            
            visited.add((i, j))

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if ni < 0 or ni >= len(grid):
                    continue 
                
                if nj < 0 or nj >= len(grid[0]):
                    continue 
                
                if grid[ni][nj] == 1: 
                    fresh -= 1
                    minutes = max(minutes, m + 1)
                    q.append((ni, nj, m + 1))
                    grid[ni][nj] = 2

        # check if any fruits are left
        return -1 if fresh > 0 else minutes
            


                






            
        
         
            