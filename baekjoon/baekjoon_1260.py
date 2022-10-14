
# link: https://www.acmicpc.net/problem/1260
# Level: S2
# DFS, BFS 기본개념

def solution():
    import sys
    input = sys.stdin.readline

    node_count, edge_count, start_node = map(int, input().split())
    edge_list = [[] for _ in range(node_count + 1)]
    edge_list[0] = None
    for _ in range(edge_count):
        edge_start, edge_end = map(int, input().split())
        edge_list[edge_start].append(edge_end)
        edge_list[edge_end].append(edge_start)

    visited_DFS = [False] * (node_count + 1)
    visited_DFS[0] = None
    visited_DFS_seq = []

    def DFS(target_node):
        if visited_DFS[target_node] is True:
            return
        visited_DFS[target_node] = True
        visited_DFS_seq.append(target_node)
        for next_node in sorted(edge_list[target_node]):
            if visited_DFS[next_node] is False:
                DFS(next_node)
    DFS(start_node)

    visited_BFS = [False] * (node_count + 1)
    visited_BFS[0] = None
    visited_BFS_seq = []
    from collections import deque
    queue_BFS = deque()

    queue_BFS.append(start_node)
    while len(queue_BFS) != 0:
        target_node = queue_BFS.popleft()
        if visited_BFS[target_node] is True:
            continue
        visited_BFS[target_node] = True
        visited_BFS_seq.append(target_node)
        for next_node in sorted(edge_list[target_node]):
            if visited_BFS[next_node] is False:
                queue_BFS.append(next_node)

    print(*visited_DFS_seq)
    print(*visited_BFS_seq)


if __name__ == "__main__":
    solution()