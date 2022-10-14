
# link: https://www.acmicpc.net/problem/19236
# Level: G2
# DFS 응용 시뮬레이션

# (row, col): None, up, up-left, left, down-left, down, down-right, right, up-right
DIRECTION = (None, (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))

def board_show(board):
    for target_row in board:
        print(target_row)
    print()

def get_pos_list_of_direction(board, row, col, direction):
    # return: list((row, col))
    pos_list = []
    while True:
        vol_row, vol_col = DIRECTION[direction]
        row += vol_row
        col += vol_col

        if board[row][col] != (-1, -1):
            pos_list.append((row, col))
        else:
            break
    return pos_list

def fish_move(board):
    #board_show(board)
    fish_list = [(0, 0) for _ in range(16 + 1)] # fish
    for row_idx in range(1, 5):
        for col_idx in range(1, 5):
            fish_num = board[row_idx][col_idx][0]
            if fish_num not in (0, 17):
                fish_list[fish_num] = (row_idx, col_idx)

    for fish_num, target_fish in enumerate(fish_list):
        if target_fish == (0, 0):
            continue
        fish_row, fish_col = target_fish
        fish_direction = board[fish_row][fish_col][1]

        for _ in range(8):
            vol_row, vol_col = DIRECTION[fish_direction]
            move_row = fish_row + vol_row
            move_col = fish_col + vol_col

            if board[move_row][move_col][0] not in (-1, 17):
                board[fish_row][fish_col], board[move_row][move_col] = board[move_row][move_col], board[fish_row][fish_col]
                fish_list[board[fish_row][fish_col][0]] = (fish_row, fish_col)
                #board_show(board)
                break
            else:
                fish_direction += 1
                if fish_direction == 9:
                    fish_direction = 1
                board[fish_row][fish_col] = (fish_num, fish_direction)



def solution():
    import sys, copy
    input = sys.stdin.readline

    board = [[(-1, -1) for _ in range(6)]] # 1~16: fish, 0: emtpy, 17: shark,
    for row_idx in range(1, 5):
        target_row = list(map(int, input().split()))
        tmp_row = []
        tmp_row.append((-1, -1))
        for col_idx in range(0, 7, 2):
            tmp_row.append((target_row[col_idx], target_row[col_idx + 1]))
        tmp_row.append((-1, -1))
        board.append(tmp_row)
    board.append([(-1, -1) for _ in range(6)])
    #board_show(board)

    max_fish = [0]
    def shark_DFS(cur_board: list, shark_row: int, shark_col: int, total_fish: int):
        shark_pos = (shark_row, shark_col, cur_board[shark_row][shark_col][1]) # row, col, direction
        cur_fish = total_fish + cur_board[shark_pos[0]][shark_pos[1]][0]
        cur_board[shark_pos[0]][shark_pos[1]] = (17, shark_pos[2])

        fish_move(cur_board)

        is_end = True
        for next_pos in get_pos_list_of_direction(cur_board, shark_pos[0], shark_pos[1], shark_pos[2]):
            if cur_board[next_pos[0]][next_pos[1]] != (0, 0):
                next_board = copy.deepcopy(cur_board)
                next_board[shark_pos[0]][shark_pos[1]] = (0, 0)
                shark_DFS(next_board, next_pos[0], next_pos[1], cur_fish)
                is_end = False

        if is_end is True:
            max_fish.append(max(max_fish.pop(), cur_fish))
            #print(max_fish)


    shark_DFS(copy.deepcopy(board), 1, 1, 0)

    print(max_fish[0])


if __name__ == "__main__":
    solution()