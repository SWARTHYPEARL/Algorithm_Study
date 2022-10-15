
# link: https://www.acmicpc.net/problem/19237
# Level: G2
# 시뮬레이션 구현

DIRECTION = (None, (-1, 0), (1, 0), (0, -1), (0, 1))

class Shark:
    def __init__(self, number = None, smell = None):
        self.number = number
        self.smell = smell

        self.position = None # (row, col)
        self.direction = None # 1: up, 2: down, 3: left, 4: right

        self.move_priority = [None]


    def get_number(self):
        return self.number
    def set_number(self, number):
        self.number = number

    def get_smell(self):
        return self.smell
    def set_smell(self, smell):
        self.smell = smell

    def get_position(self):
        return self.position
    def set_position(self, position):
        self.position = position

    def get_direction(self):
        return self.direction
    def set_direction(self, direction):
        self.direction = direction

    def get_move_priority(self):
        return self.move_priority[self.direction]
    def set_move_priority(self, move_priority):
        self.move_priority = move_priority
    def add_move_priority(self, move_priority):
        self.move_priority.append(move_priority)

    def print_status(self):
        print(f"<Shark Status - {self.number}>")
        print(f"number: {self.number}")
        print(f"smell: {self.smell}")
        print(f"position: {self.position}")
        print(f"direction: {self.direction}")
        print(f"move_priority: {self.move_priority}")
        print()

class Cell:
    def __init__(self, shark_num = None, smell = None):
        self.shark_num = shark_num # 0: emtpy, -1: unavailble
        self.smell_shark_num = shark_num
        self.smell_remain = smell

    def __str__(self):
        return f"Cell - ({self.shark_num}, {self.smell_shark_num}, {self.smell_remain})"

    def get_smell_shark_num(self):
        return self.smell_shark_num

    def is_empty(self):
        return True if self.smell_remain == 0 else False

    def in_shark(self, target_shark: Shark):
        self.shark_num = target_shark.get_number()
        self.smell_shark_num = target_shark.get_number()
        self.smell_remain = target_shark.get_smell()

    def out_shark(self):
        self.shark_num = 0

    def update(self):
        if self.shark_num == 0 and self.smell_remain > 0:
            self.smell_remain -= 1
            if self.smell_remain == 0:
                self.smell_shark_num = 0




def display_board(board):
    for row_idx in range(1, len(board) - 1):
    #for row_idx in range(0, len(board)):
        for col_idx in range(1, len(board[row_idx]) - 1):
        #for col_idx in range(0, len(board[row_idx])):
            print(board[row_idx][col_idx], end=" ")
        print()
    print()

def board_shark_update(board, shark_list):
    # shark move and update
    move_dict = {}
    for target_shark in shark_list:
        if type(target_shark) is not Shark:
            continue

        cur_row, cur_col = target_shark.get_position()

        shark_moved = False
        smell_cell = False
        while shark_moved is False:
            for next_direction in target_shark.get_move_priority():
                row_vol, col_vol = DIRECTION[next_direction]
                next_row = cur_row + row_vol
                next_col = cur_col + col_vol

                if (smell_cell is False and board[next_row][next_col].is_empty() is True) or \
                        (smell_cell is True and board[next_row][next_col].get_smell_shark_num() == target_shark.get_number()):
                    board[cur_row][cur_col].out_shark()
                    target_shark.set_position((next_row, next_col))
                    target_shark.set_direction(next_direction)
                    if (next_row, next_col) in move_dict:
                        move_dict[(next_row, next_col)].append(target_shark)
                    else:
                        move_dict[(next_row, next_col)] = [target_shark]
                    shark_moved = True
                    break

            if smell_cell is True and shark_moved is False:
                print("smell_cell - error occurred")
                display_board(board)
                exit(1)
            if shark_moved is False:
                smell_cell = True

    for target_position in move_dict.keys():
        cell_shark_list = move_dict[target_position]
        cell_remain_shark = None
        if len(cell_shark_list) != 1:
            min_shark_num = cell_shark_list[0].get_number()
            for target_cell_shark in cell_shark_list:
                min_shark_num = min(min_shark_num, target_cell_shark.get_number())

            for target_cell_shark in cell_shark_list:
                if target_cell_shark.get_number() != min_shark_num:
                    shark_list[target_cell_shark.get_number()] = None
                else:
                    cell_remain_shark = target_cell_shark
        else:
            cell_remain_shark = cell_shark_list[0]

        board[target_position[0]][target_position[1]].in_shark(cell_remain_shark)

def board_smell_update(board):
    # smell remain update

    for row_idx in range(1, len(board) - 1):
        for col_idx in range(1, len(board[row_idx]) - 1):
            board[row_idx][col_idx].update()


def solution():
    import sys
    input = sys.stdin.readline

    board_size, shark_count, smell_vol =  map(int, input().split())
    shark_list = [Shark(shark_num, smell_vol) for shark_num in range(1, shark_count + 1)]
    shark_list.insert(0, None)

    board = [[Cell(-1) for _ in range(board_size + 2)]]
    for row_idx in range(1, board_size + 1):
        target_row = list(map(int, input().split()))
        cell_list = []
        for col_idx in range(1, board_size + 1):
            if target_row[col_idx - 1] != 0:
                shark_list[target_row[col_idx - 1]].set_position((row_idx, col_idx))
                cell_list.append(Cell(target_row[col_idx - 1], smell_vol))
            else:
                cell_list.append(Cell(0, 0))
        board.append([Cell(-1)] + cell_list + [Cell(-1)])
    board.append([Cell(-1) for _ in range(board_size + 2)])

    for direction_idx, input_direction in enumerate(map(int, input().split())):
        shark_list[direction_idx + 1].set_direction(input_direction)

    for shark_idx in range(1, shark_count + 1):
        for direction_idx in range(1, 4 + 1):
            shark_list[shark_idx].add_move_priority(list(map(int, input().split())))

    #display_board(board)

    sec = 0
    while shark_list.count(None) != len(shark_list) - 1 and sec <= 1000:

        board_shark_update(board, shark_list)
        sec += 1

        board_smell_update(board)
        #print(f"----sec: {sec}")
        #display_board(board)
        #print()


    print(sec) if sec <= 1000 else print(-1)


if __name__ == "__main__":
    solution()