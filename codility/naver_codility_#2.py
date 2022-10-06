# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def print_board(board):
    for height_idx in reversed(range(len(board))):
        print(board[height_idx])

def solution(A):
    # write your code in Python 3.6

    # draw width x height board  
    # one for line, zero for nothing
    width = len(A)
    height = max(A)
    board = [[0] * width for _ in range(height)]
    #print("<<board generate>>")
    #print(board)

    # bottom line for 1
    for width_idx, target_A in enumerate(A):
        for height_idx in range(target_A):
            board[height_idx][width_idx] = 1
    #print("<<board initialize>>")
    #print_board(board)

    # count line of ones per horinotal line
    total_stripe_count = 0
    for height_idx, horizontal_line in enumerate(board):
        stripe_count = 0

        horiz_str = "".join(str(s) for s in horizontal_line)
        zero_idx = horiz_str.find("0")
        if zero_idx <= -1:
            stripe_count += 1
        else:
            while True:
                one_idx = horiz_str.find("1", zero_idx + 1)
                if one_idx <= -1:
                    break

                zero_idx = horiz_str.find("0", one_idx + 1)
                stripe_count += 1
                if zero_idx <= -1:
                    break

        #print(f"height - [{height_idx}]'s stripe count: {stripe_count}")
        total_stripe_count += stripe_count

    return total_stripe_count



if __name__ == "__main__":
    print(solution([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]))