class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {i: [] for i in range(numCourses)}
        for course, depend in prerequisites:
            d[course].append(depend)

            
        visited = set()
        def dfs(cur):
            if cur in visited:
                return False
            if d[cur] == []:
                return True

            visited.add(cur)
            for depend in d[cur]:
                if not dfs(depend):
                    return False
            visited.remove(cur)
            d[cur] == []
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
                
        