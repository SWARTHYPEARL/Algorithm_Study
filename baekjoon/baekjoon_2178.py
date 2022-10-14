
# link: https://www.acmicpc.net/problem/2178
# Level: S1
# 최소노드 -> BFS, python 문법센스가 있을수록 간결해질듯?

def solution():
    import sys
    input = sys.stdin.readline

    height, width = map(int, input().split())
    board = [[0] * (width + 2)] # 0: unavailable, 1: available, 2: visited
    for _ in range(height):
        board.append([0] + list(map(int, list(input().rstrip()))) + [0])
    board.append([0] * (width + 2))
    goal_node = (height, width) # height, width

    from collections import deque
    queue_BFS = deque()
    queue_BFS.append((1, 1, 1)) # height, width, depth
    while len(queue_BFS) != 0:
        target_node = queue_BFS.popleft()
        if board[target_node[0]][target_node[1]] == 2:
            continue

        board[target_node[0]][target_node[1]] = 2
        if target_node[:2] == goal_node:
            print(target_node[2])
            break

        check_node_list = (
            (target_node[0] - 1, target_node[1]), # up
            (target_node[0] + 1, target_node[1]), # down
            (target_node[0], target_node[1] - 1), # left
            (target_node[0], target_node[1] + 1) # right
        )
        for next_node in check_node_list:
            if board[next_node[0]][next_node[1]] == 1:
                queue_BFS.append(((*next_node, target_node[2] + 1)))



if __name__ == "__main__":
    solution()