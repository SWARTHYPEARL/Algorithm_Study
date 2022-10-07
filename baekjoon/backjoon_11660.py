
# link: https://www.acmicpc.net/problem/11660
# 2차원 부분합 알고리즘

def show_table(target_table):
    print("--------------------")
    for target_row in target_table:
        print(target_row)
    print("--------------------")


def solution():
    import sys
    input = sys.stdin.readline

    table_size, cal_count = map(int, input().split())
    total_table = []
    total_table.append([0] * (table_size + 1))
    for _ in range(table_size):
        total_table.append([0] + list(map(int, input().split())))
    #show_table(total_table)

    sum_table = []
    sum_table.append([0] * (table_size + 1))
    for target_row in range(1, table_size + 1):
        tmp_row = [0]
        for target_col in range(1, table_size + 1):
            tmp_row.append(total_table[target_row][target_col] + tmp_row[target_col - 1] + sum_table[target_row - 1][target_col] - sum_table[target_row - 1][target_col - 1])
        sum_table.append(tmp_row.copy())
        del tmp_row
    #show_table(sum_table)

    for _ in range(cal_count):
        start_row, start_col, end_row, end_col = map(int, input().split())

        #print(f"plus: {sum_table[end_row][end_col]}")
        #print(f"minus: {sum_table[end_row][start_col - 1]}")
        #print(f"minus: {sum_table[start_row - 1][end_col]}")
        #print(f"plus: {sum_table[start_row -1][start_col - 1]}")
        print(sum_table[end_row][end_col] - sum_table[end_row][start_col - 1] - sum_table[start_row - 1][end_col] + sum_table[start_row -1][start_col - 1])
        

if __name__ == "__main__":
    solution()