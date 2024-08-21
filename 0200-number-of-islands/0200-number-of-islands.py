from collections import deque

class Solution(object):
    def numIslands(self, grid):
        answer = 0
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        dr = [1, 0, -1, 0]
        dc = [0, -1, 0, 1]
        
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited[r][c] = True
            
            while q:
                cur_r, cur_c = q.popleft()
                for i in range(4):
                    next_r = cur_r + dr[i]
                    next_c = cur_c + dc[i]
                    if 0 <= next_r < n and 0 <= next_c < m and grid[next_r][next_c] == "1":
                        if not visited[next_r][next_c]:
                            q.append((next_r, next_c))
                            visited[next_r][next_c] = True
        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1" and not visited[r][c]:
                    bfs(r,c)
                    answer += 1
                    
        return answer