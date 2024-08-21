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
        # all함수 -> visited에 하나라도 False가 있으면 False를 return, 전체가 다 True일 때만 True를 return
        return all(visited)
                