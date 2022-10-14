
# link: https://www.acmicpc.net/problem/16236
# Level: G3
# BFS 응용 시뮬레이션
# queue로 삽질하지말고 우선순위 heap 응용.

def board_show(board):
    for row in board[1:len(board) - 1]:
        print(row[1:len(row) - 1])

def solution():
    import sys, heapq
    input = sys.stdin.readline

    board_size = int(input())
    board = [[-1] * (board_size + 2)]
    shark_list = [0] * 7
    baby_pos = None
    for row in range(board_size):
        target_row = list(map(int, input().split()))
        for col, target_element in enumerate(target_row):
            if target_element == 9:
                baby_pos = (row + 1, col + 1)
            elif target_element > 0:
                shark_list[target_element] += 1
        board.append([-1] + target_row + [-1])
    board.append([-1] * (board_size + 2))

    cur_size = 2
    cur_eaten = 0
    cur_time = 0
    visited_list = [[False] * (board_size + 2) for _ in range(board_size + 2)]

    def shark_BFS(row, col, size_limit: int):
        # return row, col, depth of the closest eatable shark
        # if not: return -1 -1, 0
        queue_BFS = []
        heapq.heappush(queue_BFS, ("{0:02d}{1:02d}{2:02d}".format(0, row, col), (row, col, 0)))

        while len(queue_BFS) != 0:
            target_row, target_col, cur_depth = heapq.heappop(queue_BFS)[1]
            if visited_list[target_row][target_col] is True:
                continue

            visited_list[target_row][target_col] = True
            if board[target_row][target_col] not in (0, 9, size_limit):
                return target_row, target_col, cur_depth

            cur_depth += 1
            move_list = (
                (target_row - 1, target_col, cur_depth), # up
                (target_row, target_col - 1, cur_depth), # left
                (target_row, target_col + 1, cur_depth), # right
                (target_row + 1, target_col, cur_depth) # down
            )
            for move_idx, next_move in enumerate(move_list):
                if -1 < board[next_move[0]][next_move[1]] <= size_limit or board[next_move[0]][next_move[1]] == 9:
                    #queue_BFS.append(next_move)
                    heapq.heappush(queue_BFS, ("{0:02d}{1:02d}{2:02d}".format(next_move[2], next_move[0], next_move[1]), next_move))

        return -1, -1, 0


    while True:
        shark_row, shark_col, move_count = shark_BFS(baby_pos[0], baby_pos[1], cur_size)
        visited_list = [[False] * (board_size + 2) for _ in range(board_size + 2)]
        if (shark_row, shark_col, move_count) == (-1, -1, 0):
            break

        #print(board_show(board))
        #print((shark_row, shark_col, move_count, cur_size))
        #print()
        #input()

        cur_time += move_count
        shark_list[board[shark_row][shark_col]] -= 1
        board[baby_pos[0]][baby_pos[1]] = 0
        board[shark_row][shark_col] = 9
        baby_pos = (shark_row, shark_col)
        cur_eaten += 1
        if cur_size == cur_eaten:
            cur_size += 1
            cur_eaten = 0

    print(cur_time)


if __name__ == "__main__":
    solution()