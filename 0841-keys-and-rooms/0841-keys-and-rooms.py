class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = [False] * n

        def dfs(cur_v, rooms, visited):
            visited[cur_v] = True
            for next_v in rooms[cur_v]:
                if not visited[next_v]:
                    dfs(next_v, rooms, visited)
        dfs(0, rooms, visited)

        for v in visited:
            if not v:
                return False
        return True