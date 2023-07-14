import collections


def courseSchedule(numCourses, prerequisites):
    objList = collections.defaultdict(list)

    for course, pre in prerequisites:
        objList[pre].append(course)

    def cycle(node, tracker, visited):
        tracker[node] = True
        visited[node] = True

        for n in objList[node]:
            if n not in visited and cycle(n, tracker, visited):
                return True
            elif n in tracker:
                return True
        tracker.pop(node)

    visited = {}
    for n in range(numCourses):
        tracker = {}
        if n not in visited and cycle(n, tracker, visited):
            return False
    return True


print(courseSchedule(2, [[1, 0]]))
print(courseSchedule(2, [[1,0], [0,1]]))
