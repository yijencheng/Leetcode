## TLE
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # d = {}
        # for course, depend in prerequisites: #wrong
        #     if course not in d:
        #         d[course] = []
        #     d[course].append(depend)

        d = {i: [] for i in range(numCourses)}
        for course, depend in prerequisites:
            d[course].append(depend)

        loop = [False]
        visited = set()
        def dfs(cur):
            if loop[0]:
                return
            if cur in visited:
                loop[0] = True
                return
            if d[cur] == []:
                return

            visited.add(cur)
            for depend in d[cur]:
                dfs(depend)
            visited.remove(cur)
            d[cur] == []
            
        for c in range(numCourses):
            dfs(c)
            if loop[0]:return False
        return True
                
        