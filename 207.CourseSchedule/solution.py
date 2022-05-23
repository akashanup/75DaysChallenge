import unittest


class Solution:
    def isCyclic(self, graph, v, visited, lookup):
        visited[v] = True
        lookup[v] = True
        cycle = False
        for u in graph[v]:
            if lookup[u]:
                cycle = True
            elif not visited[u]:
                cycle = self.isCyclic(graph, u, visited, lookup)

            if cycle:
                break
        lookup[v] = False
        return cycle

    def canFinish(self, numCourses: int, prerequisites) -> bool:
        courses = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            courses[v].append(u)

        visited = [False] * numCourses
        lookup = [False] * numCourses

        for v in range(numCourses):
            if not visited[v] and self.isCyclic(courses, v, visited, lookup):
                return False

        return True


class Test(unittest.TestCase):
    def testCanFinish1(self):
        actual = Solution().canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]])
        expected = True
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
