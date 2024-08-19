from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        # 초기 설정
        answer = 0
        n = len(grid)
        q = deque()
        dr = [1, 0, -1, 0, 1, 1, -1, -1]
        dc = [0, 1, 0, -1, 1, -1, 1, -1]
        visited = [[False] * n for _ in range(n)]

        # 시작점 예약
        if grid[0][0] == 0:  # 시작점이 (1,1)이면 안되므로 (0,0)일 때만 실행되도록 설정
            q.append((0, 0, 1))
            visited[0][0] = True

        while q:
            # 방문
            r, c, dist = q.popleft()
            if r == n-1 and c == n-1: # 도착지점(n-1, n-1)일 경우 현재 거리 return
                return dist

            # 예약
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    if not visited[nr][nc]:
                        q.append((nr, nc, dist+1))
                        visited[nr][nc] = True
                        
        return -1
