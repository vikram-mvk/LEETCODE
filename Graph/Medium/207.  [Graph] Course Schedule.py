'''
Topological Sort based qn: Can be done by BFS (Kahn's Algo) and DFS
https://www.youtube.com/watch?v=u4v_kvOfumU&t=199s

Famous problem, so see multiple approches (BFS and DFS)

This question is asking if the graph has a cycle or not

Algorithm:

1. create a 2d matrix with indices representing courses and its values are the courses that depend on it
so, indices act as pre-requisite courses.

2. The courses in graph's ith index,
3. Increase the dependency value for each node added to a pre requisite's course list

4. if an index has dependency = 0, then such courses can be completed first

5. Add such courses in a queue and the complete the courses that are dependent on them as well


'''

def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # we need to maintain to things
    # prerequisite course to dependent course mapping
    # dependent course has how many prerequisite. is it 1 or 2 or 3?

    graph = [[] for i in range(numCourses)]
    # Index represents courses and values at index represents courses that depend on indexed course

    dependent_on = [0] * numCourses
    # Initially all courses have no dependency. When a course has a new prerequisite, increase by 1

    for i in range(len(prerequisites)):
        # in the prerequisite index, add this course
        graph[prerequisites[i][1]].append(prerequisites[i][0])

        # increase the dependency count (prerequisite count) of the current course
        dependent_on[prerequisites[i][0]] += 1

    completed = []

    # now we have the courses and its dependency count, add the courses with 0 dependency to completed
    for i, x in enumerate(dependent_on):
        if x == 0:
            completed.append(i)
            numCourses -= 1

    # now for each completed course, if that one is prerequisite, the course dependent on it will get its dependency reduced by 1

    while len(completed):
        temp = graph[completed.pop()]
        # this will get all the courses that were dependent on the completed course

        for x in temp:
            dependent_on[x] -= 1
            if dependent_on[x] == 0:
                completed.append(x)
                numCourses -= 1

    return numCourses == 0



