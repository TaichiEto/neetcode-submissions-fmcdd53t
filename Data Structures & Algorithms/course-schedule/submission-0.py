import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        graph = collections.defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        
        queue = collections.deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        taken_courses = 0

        while queue:
            current_course = queue.popleft()
            taken_courses += 1

            for next_course in graph[current_course]:
                in_degree[next_course] -= 1

                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        return taken_courses == numCourses