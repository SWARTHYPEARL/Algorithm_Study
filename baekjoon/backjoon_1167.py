
# link: https://www.acmicpc.net/problem/1167
# Level: G3
# 트리 특징 + DFS or BFS에 weight 추가
# 탐색 알고리즘 2번으로 지름 노드 찾아내기 <- 핵심 아이디어

def solution():
    import sys
    input = sys.stdin.readline

    node_count = int(input())
    edge_list = [[] for _ in range(node_count + 1)]
    for _ in range(node_count):
        target_edge_list = list(map(int, input().split()))
        target_node = target_edge_list[0]
        for target_edge_idx in range(1, len(target_edge_list) - 1, 2):
            edge_list[target_node].append((target_edge_list[target_edge_idx], target_edge_list[target_edge_idx + 1]))

    visited_list = [False] * (node_count + 1)
    max_weight_list = [0] * (node_count + 1)
    def DFS(target_node: tuple, edge_weight: int):
        # target_node: (node, before_edge_weight)
        # edge_weight: cur_edge_weight
        if visited_list[target_node[0]] is True:
            return

        visited_list[target_node[0]] = True
        edge_weight += target_node[1]
        if max_weight_list[target_node[0]] < edge_weight:
            max_weight_list[target_node[0]] = edge_weight

        for next_node in edge_list[target_node[0]]:
            if visited_list[next_node[0]] is False:
                DFS(next_node, edge_weight)

    DFS((1, 0), 0)
    max_node_idx = max_weight_list.index(max(max_weight_list))

    visited_list = [False] * (node_count + 1)
    DFS((max_node_idx, 0), 0)

    print(max(max_weight_list))


if __name__ == "__main__":
    solution()