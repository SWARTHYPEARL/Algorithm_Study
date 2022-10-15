
# link: https://www.acmicpc.net/problem/20056
# Level: G4
# 시뮬레이션 구현

DIRECTION = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

class FireBall:
    def __init__(self, m, s, d):
        self.mass = m
        self.speed = s
        self.direction = d

    def __str__(self):
        return f"({self.mass}, {self.speed}, {self.direction})"

    def get_mass(self):
        return self.mass

    def get_speed(self):
        return self.speed

    def get_direction(self):
        return self.direction


def display_board(board):
    for row_idx in range(len(board)):
        print("[", end="")
        for col_idx in range(len(board[row_idx])):
            print("[", end="")
            for target_fire in board[row_idx][col_idx]:
                print(target_fire, end=" ")
            print("], ", end="")
        print("]")
    print()

def fire_move(board):
    move_dict = {}
    for board_row_idx in range(len(board)):
        for board_col_idx in range(len(board[board_row_idx])):
            for fire_idx in range(len(board[board_row_idx][board_col_idx])):
                target_fire = board[board_row_idx][board_col_idx][fire_idx]
                row_direction, col_direction = DIRECTION[target_fire.get_direction()]
                row_vol = row_direction * target_fire.get_speed()
                col_vol = col_direction * target_fire.get_speed()

                next_row = (board_row_idx + row_vol) % len(board)
                next_col = (board_col_idx + col_vol) % len(board[board_row_idx])

                if (next_row, next_col) in move_dict:
                    move_dict[(next_row, next_col)].append(target_fire)
                else:
                    move_dict[(next_row, next_col)] = [target_fire]

    # update board with moved fireball
    for board_row_idx in range(len(board)):
        for board_col_idx in range(len(board[board_row_idx])):
            if (board_row_idx, board_col_idx) in move_dict:
                board[board_row_idx][board_col_idx] = move_dict[(board_row_idx, board_col_idx)]
            else:
                board[board_row_idx][board_col_idx] = []

def board_update(board):
    for board_row_idx in range(len(board)):
        for board_col_idx in range(len(board[board_row_idx])):
            fire_list = board[board_row_idx][board_col_idx]
            if len(fire_list) > 1:
                total_mass = 0
                total_speed = 0
                total_direction_list = []
                for target_fire in fire_list:
                    total_mass += target_fire.get_mass()
                    total_speed += target_fire.get_speed()
                    total_direction_list.append(target_fire.get_direction() % 2)

                total_mass = int(total_mass / 5)
                total_speed = int(total_speed / len(fire_list))
                total_direction_list = [1, 3, 5, 7] if 1 in total_direction_list and 0 in total_direction_list else [0, 2, 4, 6]

                new_fire_list = []
                if total_mass != 0:
                    for new_idx in range(4):
                        new_fire_list.append(FireBall(total_mass, total_speed, total_direction_list[new_idx]))
                board[board_row_idx][board_col_idx] = new_fire_list

def total__fireball_mass(board):
    mass = 0
    for target_row in board:
        for target_fire_list in target_row:
            for target_fire in target_fire_list:
                mass += target_fire.get_mass()

    return mass

def solution():
    import sys
    input = sys.stdin.readline

    board_size, fire_count, move_count = map(int ,input().split())
    board = [[[] for _ in range(board_size)] for _ in range(board_size)]
    for _ in range(fire_count):
        target_row, target_col, target_mass, target_speed, target_direction = map(int, input().split())
        board[target_row - 1][target_col - 1].append(FireBall(target_mass, target_speed, target_direction))
    #display_board(board)

    for _ in range(move_count):
        fire_move(board)
        #display_board(board)

        board_update(board)
        #display_board(board)
        #print("-------------------------------------")

    print(total__fireball_mass(board))


if __name__ == "__main__":
    solution()