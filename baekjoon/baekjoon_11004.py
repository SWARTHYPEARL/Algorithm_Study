
# link: https://www.acmicpc.net/problem/11004
# Level: S5
# 퀵 정렬: 오름차순

from collections import deque

def quick_sort(target_deque: deque):
    if len(target_deque) == 0:
        return deque()
    pivot_value = target_deque.pop()

    quick_left = deque()
    quick_right = deque()
    for target_value in target_deque:
        if target_value < pivot_value:
            quick_left.append(target_value)
        else:
            quick_right.append(target_value)

    return quick_sort(quick_left) + deque([pivot_value]) + quick_sort(quick_right)

def quick_sort2(target_deque: deque, start_idx: int, end_idx: int):
    if start_idx >= end_idx:
        return

    cur_start_idx = start_idx
    cur_end_idx = end_idx

    pivot_idx = start_idx
    start_idx += 1
    while start_idx != end_idx:
        if target_deque[start_idx] < target_deque[pivot_idx]:
            start_idx += 1
        else:
            if target_deque[end_idx] >= target_deque[pivot_idx]:
                end_idx -= 1
            else:
                target_deque[start_idx], target_deque[end_idx] = target_deque[end_idx], target_deque[start_idx]
                start_idx += 1

    # pivot index
    if target_deque[start_idx] < target_deque[pivot_idx]:
        if start_idx == len(target_deque) - 1:
            target_deque.append(target_deque.popleft())
        else:
            target_deque.insert(start_idx + 1, target_deque[pivot_idx])
            target_deque.popleft()
        pivot_idx = start_idx + 1
    else:
        target_deque.insert(start_idx, target_deque[pivot_idx])
        target_deque.popleft()
        pivot_idx = start_idx - 1

    quick_sort2(target_deque, cur_start_idx, pivot_idx - 1)
    quick_sort2(target_deque, pivot_idx + 1, cur_end_idx)


def solution():
    import sys
    sys.setrecursionlimit(10000)
    input = sys.stdin.readline

    num_count, num_rank = map(int, input().split())
    num_deque = deque(map(int, input().split()))

    #num_deque = quick_sort(num_deque)
    quick_sort2(num_deque, 0, len(num_deque) - 1)

    print(num_deque[num_rank - 1])


if __name__ == "__main__":
    solution()