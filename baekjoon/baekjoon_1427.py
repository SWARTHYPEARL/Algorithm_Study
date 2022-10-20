
# link: https://www.acmicpc.net/problem/1427
# Level: S5
# 선택정렬 구현: 내림차순

def solution():
    import sys
    input = sys.stdin.readline

    num_list = list(map(int, list(input().rstrip())))

    for loop_idx in range(len(num_list)):
        max_idx = loop_idx
        for target_idx in range(loop_idx + 1, len(num_list)):
            if num_list[max_idx] < num_list[target_idx]:
                max_idx = target_idx

        if max_idx != loop_idx:
            num_list[max_idx], num_list[loop_idx] = num_list[loop_idx], num_list[max_idx]

    for target_num in num_list:
        print(target_num, end="")


if __name__ == "__main__":
    solution()