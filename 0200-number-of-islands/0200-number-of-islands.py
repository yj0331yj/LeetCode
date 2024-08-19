from collections import deque

class Solution(object):
    def numIslands(self, grid):
        answer = 0
        row_len, col_len = len(grid), len(grid[0])
        visited = [[False] * col_len for _ in range(row_len)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
    
        def bfs(r, c):
            # 초기 세팅
            q = deque()
            # 시작점 예약
            q.append((r, c))
            visited[r][c] = True

            while q:
                # 현재 노드 방문
                cur_r, cur_c = q.popleft()
                # 다음 노드 예약
                for i in range(4):
                    next_r = cur_r + dr[i]
                    next_c = cur_c + dc[i]
                    if 0 <= next_r < row_len and 0 <= next_c < col_len and grid[next_r][next_c] == "1":
                        if not visited[next_r][next_c]:
                            q.append((next_r, next_c))
                            visited[next_r][next_c] = True
                            
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == "1" and not visited[r][c]:
                    bfs(r,c)
                    answer += 1
        
        return answer