'''
UNDERSTAND:
- Inputs: Given an integer numCourses which is the number of courses you have to finish and a 2d list prerequisites [a_i, b_i] where in order to take a_i, you have to take b_i
- Have to see if we can complete all courses which are from 0 to numCourses - 1 while satisfying the prereqs
- Output: If we can finish all courses we return true else false
- Ex 2 is false because you have to take course 1 before course 0 and course 0 before course 1 which is impossible and creates an infinite loop
- How big can numCourses be? 1 <= numCourses <= 2000
- How about prereqs? 0 <= prerequisites.length <= 5000
- So prereqs[i] can only have two values? and those values are 0 to numCourses - 1? Yes for both
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique.
- So pretty much as soon as we find a loop between 2 prereqs we know it is false
- It is not necessary for all courses to have a prereq
- Can len(prereqs) be > numCourses? Yes
- If we have same number in both prereqs[i] that is another impossible situation
- Could a course have multiple prerequisites? Yes, like [[2,1], [2,0]] means course 2 needs both 1 and 0
- Could a course be a prerequisite for multiple other courses? Yes, like [[1,0], [2,0]] means course 0 is needed for both 1 and 2
- Could we have longer chains of dependencies? Yes, like [[1,0], [2,1], [3,2]] creates a chain where 3 ultimately depends on 0
- numCourses = 0 will return True

MATCH:
- What are we trying to achieve? All we have to do is ensure the prereqs go fine and dont create an impossible loop, rest is covered by constraints
- So core task is cycle detection
- We can run DFS on each course to check its prereqs and its prereqs prereqs so on and so forth to see if a cycle exists anywhere

PLAN:
- A hashmap which maps out all courses and their prereqs
- Map everything in a loop
- A visit set, which keeps track of all visited courses in a path, this will help us detect a cycle
- Dfs function with a course as parameter
    - Base case: if curr crs already in visit set, it means a cycle detected return false
    - Base case: If curr crs does not have prereqs, it's valid, return True
    - If no base case hit, add this crs to visit set and run dfs on its prereqs
    - Once you come back from its prereqs you can remove this course from path because it is valid
    - Similarly you can remove all its prereqs from hashmap because now we know, no matter what this course can be completed
    - return True

- Loop over all courses and send them to dfs function, if dfs function returns false, instantly return it
- return True

EVALUATE:
- I knew I had to use DFS but clearing out the prereqs after validating a course and using visit set was confusing
- TC: O(V + E) for visiting all nodes and edges
- SC: O(V + E) hashmap stores the whole graph
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visit = set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True

            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True