"""
https://neetcode.io/problems/course-schedule/question

Video: https://www.youtube.com/watch?v=EgI5nU9etnU

Course Schedule

You are given an array prerequisites where prerequisites[i] = [a, b]
indicates that you must take course b first if you want to take course a.

The pair [0, 1], indicates that must take course 1 before taking course 0.

There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return true if it is possible to finish all courses, otherwise return false.

Example 1:
Input: numCourses = 2, prerequisites = [[0,1]]
Output: true
Explanation: First take course 1 (no prerequisites) and then take course 0.

Example 2:
Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
Output: false
Explanation: In order to take course 1 you must take course 0, and to take course 0 you must take course 1.
So it is impossible.

Constraints:
1 <= numCourses <= 1000
0 <= prerequisites.length <= 1000
prerequisites[i].length == 2
0 <= a[i], b[i] < numCourses
All prerequisite pairs are unique.
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dependency_map = {}
        # course: [[0,1],[0,2],[1,3],[1,4],[3,4]] -> TRUE
        # {0: [1, 2], 1: [3, 4], 2: [], 3: [4], 4: []}
        #
        # course: [[0,1],[1,2],[2,0]] -> FALSE
        # {0: [1], 1: [2], 2: [0]}

        # pre_map: {0: [], 1: [], 2: [], 3: [], 4: []}
        pre_map = {i:[] for i in range(numCourses)}
        print(f"pre_map: {pre_map}")
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        print("=====")
        print(f"pre_map1: {pre_map}")

        visit_set = set()
        def dfs(crs):
            print(f"----- -----CRS2: {crs} ----- -----")
            print(f"pre_map2: {pre_map}")
            print(f"visit_set1: {visit_set}")

            if crs in visit_set:
                print(f"Course {crs} has a circular dependency. Return False.")
                return False

            if not pre_map[crs]:
                print(f"Course {crs} does not have any dependencies. Return True.")
                return True

            visit_set.add(crs) # add the course to the visited list
            print("----- ----- -----")
            print(f"visit_set2: {visit_set}")
            for prerequisite in pre_map[crs]:
                print(f"----- prerequisite: {prerequisite} -----")
                print(f"visit_set3: {visit_set}")
                if not dfs(prerequisite): return False

            visit_set.remove(crs) # remove the course from the visited list
            print("-----")
            print(f"visit_set4: {visit_set}")

            pre_map[crs] = []
            print("=====")
            print(f"pre_map3: {pre_map}")
            return True

        for crs in range(numCourses):
            print(f"----- ----- CRS1: {crs} ----- -----")
            if not dfs(crs): return False
        return True

Solution().canFinish(numCourses=3, prerequisites=[[0,1],[1,2],[2,0]])
Solution().canFinish(numCourses=5, prerequisites=[[0,1],[0,2],[1,3],[1,4],[3,4]])
