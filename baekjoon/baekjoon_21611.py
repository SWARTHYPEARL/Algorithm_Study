
# link: https://www.acmicpc.net/problem/21611
# Level: G1

from collections import deque

def display_board(board):
    for target_row in board:
        print(target_row)

def spiral_index(length: int, pos):
    ldru_switch = deque([1, 0, 0, 0])
    move_vol = 1
    cur_pos = [pos[0], pos[1]]
    pos_list = [cur_pos.copy()]
    spiral_idx = 0
    while len(pos_list) < length:
        for _ in range(move_vol):
            if ldru_switch.index(1) == 0:
                cur_pos[1] -= 1
            elif ldru_switch.index(1) == 1:
                cur_pos[0] += 1
            elif ldru_switch.index(1) == 2:
                cur_pos[1] += 1
            elif ldru_switch.index(1) == 3:
                cur_pos[0] -= 1
            pos_list.append(cur_pos.copy())
            if len(pos_list) == length:
                break

        ldru_switch.rotate(1)
        move_vol += spiral_idx % 2
        spiral_idx += 1

    return pos_list

def solution():

    board_size = 5

    target_deque = deque(range(board_size ** 2 - 15))
    #print(target_deque)

    board = [[0] * board_size for _ in range(board_size)]
    #print(board)
    #display_board(board)

    spiral_list = spiral_index(len(target_deque), (board_size // 2, board_size // 2))
    for target_idx, target_spiral in enumerate(spiral_list):
        board[target_spiral[0]][target_spiral[1]] = target_deque[target_idx]
    display_board(board)


if __name__ == "__main__":
    solution()