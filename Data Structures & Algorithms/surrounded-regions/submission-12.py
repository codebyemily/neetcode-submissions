class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        # for every O that is reachable by the border turn it into "#"
        def dfs(i, j):
            if (i, j) in visited: 
                return 
            
            visited.add((i, j))
            board[i][j] = "#"

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if ni < 0 or ni >= rows: 
                    continue
                
                if nj < 0 or nj >= cols:
                    continue 
                
                if board[ni][nj] == "O":
                    dfs(ni, nj)

        # activate borders 
        for r in range(len(board)):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)

        # top and bottom borders
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O": 
                    board[i][j] = 'X'
                elif board[i][j] == "#":
                    board[i][j] = "O"