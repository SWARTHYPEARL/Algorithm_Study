
# link: https://www.acmicpc.net/problem/2751
# Level: S5
# 병합 정렬 구현: 오름차순
# index로 장난질을 해야 속도를 올릴 수 있음
# 그냥 우선순위큐로 해결

from collections import deque

def merge_sort(target_deque: deque, start_idx: int, end_idx: int):
    if start_idx == end_idx:
        return
    half_idx = (start_idx + end_idx) // 2
    merge_sort(target_deque, start_idx, half_idx)
    merge_sort(target_deque, half_idx + 1, end_idx)

    # half_A setting
    half_A_idx = start_idx
    half_A_end = half_idx

    # half_B setting
    half_B_idx = half_idx + 1
    half_B_end = end_idx

    merge_deque = deque()
    while True:
        if half_A_idx > half_A_end and half_B_idx > half_B_end:
            break

        if half_A_idx <= half_A_end and half_B_idx <= half_B_end:
            if target_deque[half_A_idx] < target_deque[half_B_idx]:
                merge_deque.append(target_deque[half_A_idx])
                half_A_idx += 1
            else:
                merge_deque.append(target_deque[half_B_idx])
                half_B_idx += 1
        elif half_A_idx <= half_A_end:
            merge_deque.append(target_deque[half_A_idx])
            half_A_idx += 1
        else:
            merge_deque.append(target_deque[half_B_idx])
            half_B_idx += 1

    target_idx = start_idx
    for target_value in merge_deque:
        target_deque[target_idx] = target_value
        target_idx += 1


def solution():
    import sys, heapq
    sys.setrecursionlimit(1000000)
    input = sys.stdin.readline

    #num_count = int(input())
    #num_deque = deque()
    #for _ in range(num_count):
    #    num_deque.append(int(input()))

    #merge_sort(num_deque, 0, len(num_deque) - 1)

    #for target_value in num_deque:
    #    print(target_value)

    num_count = int(input())
    heapq_list = []
    for _ in range(num_count):
        heapq.heappush(heapq_list, int(input()))

    for _ in range(num_count):
        print(heapq.heappop(heapq_list))


if __name__ == "__main__":
    solution()