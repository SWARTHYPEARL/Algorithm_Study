
# Link: https://school.programmers.co.kr/learn/courses/30/lessons/43162


def DFS(graph, v, visited):
    visited[v] = True

    for com_idx, connected in enumerate(graph[v]):
        if connected == 1 and visited[com_idx] is False:
            DFS(graph, com_idx, visited)

def solution(n, computers):
    answer = 0

    visited = [False] * n

    count_DFS = 0
    start_DFS = 0
    while True:
        DFS(computers, start_DFS, visited)
        count_DFS += 1

        if False in visited:
            start_DFS = visited.index(False)
        else:
            break

    answer = count_DFS

    return answer