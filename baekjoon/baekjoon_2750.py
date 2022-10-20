
# link: https://www.acmicpc.net/problem/2750
# Level: B2
# 버블정렬 구현: 오름차순

def solution():
    import sys
    input = sys.stdin.readline
    
    num_count = int(input())
    from collections import deque
    num_list = deque()
    for _ in range(num_count):
        num_list.append(int(input()))

    for loop_idx in range(num_count):
        for list_idx in range(num_count - loop_idx - 1):
            if num_list[list_idx] > num_list[list_idx + 1]:
                num_list[list_idx], num_list[list_idx + 1] = num_list[list_idx + 1], num_list[list_idx]

    for target_num in num_list:
        print(target_num)

if __name__ == "__main__":
    solution()