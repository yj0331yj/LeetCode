from collections import deque

class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = [False] * n

        def bfs(start_v):
            q = deque()
            q.append(start_v)
            visited[start_v] = True

            while q:
                cur_v = q.popleft()
                for next_v in rooms[cur_v]:
                    if not visited[next_v]:
                        q.append(next_v)
                        visited[next_v] = True

        bfs(0)
                        
        for v in visited:
            if not v:
                return False
        return True
        