
# link: https://www.acmicpc.net/problem/11724
# Level: S5
# DFS 이용. 양뱡향 엣지임을 주의
# 재귀함수를 사용할 때, sys.setrecursionliit(10000) 설정!!

def solution():
    import sys
    input = sys.stdin.readline

    node_count, edge_count = map(int, input().split())
    edge_list = [None] * (node_count + 1)
    for _ in range(edge_count):
        edge_start, edge_end = map(int, input().split())
        if edge_list[edge_start] is None:
            edge_list[edge_start] = [edge_end]
        else:
            edge_list[edge_start].append(edge_end)
        if edge_list[edge_end] is None:
            edge_list[edge_end] = [edge_start]
        else:
            edge_list[edge_end].append(edge_start)

    node_list = [False] * (node_count + 1)
    node_list[0] = None
    count_CC = 0
    from collections import deque
    stack_dfs = deque()
    while False in node_list:
        target_node = node_list.index(False)

        count_CC += 1
        node_list[target_node] = True
        if edge_list[target_node] is not None:
            for target_edge in edge_list[target_node]:
                stack_dfs.append(target_edge)
        while len(stack_dfs) != 0:
            target_stack_node = stack_dfs.pop()

            if node_list[target_stack_node] is False:
                node_list[target_stack_node] = True
                if edge_list[target_stack_node] is not None:
                    for target_stack_edge in edge_list[target_stack_node]:
                        stack_dfs.append(target_stack_edge)

    print(count_CC)


def solution_2nd():
    import sys
    sys.setrecursionlimit(10000)
    input = sys.stdin.readline

    node_count, edge_count = map(int, input().split())
    node_list = [[] for _ in range(node_count + 1)]
    visited_list = [False] * (node_count + 1)

    for _ in range(edge_count):
        edge_start, edge_end = map(int, input().split())
        node_list[edge_start].append(edge_end)
        node_list[edge_end].append(edge_start)

    def DFS(cur_node):
        visited_list[cur_node] = True
        for next_node in node_list[cur_node]:
            if visited_list[next_node] is False:
                DFS(next_node)

    count_CC = 0
    for target_node in range(1, node_count + 1):
        if visited_list[target_node] is False:
            count_CC += 1
            DFS(target_node)
        else:
            continue

    print(count_CC)


if __name__ == "__main__":
    #solution()
    solution_2nd()