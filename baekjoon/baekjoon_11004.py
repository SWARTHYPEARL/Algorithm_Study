
# link: https://www.acmicpc.net/problem/11004
# Level: S5
# 퀵 정렬: 오름차순
# index 장난질을 통해 리스트 append & pop 작동을 최소화
# 그래도 안되서 quick_select 알고리즘 구현
# quick_select 도 최악은 n^2... 그냥 문제풀이용으로 pivot을 꼬아서 선택할 것
# 안되서 걍 내장함수 sorted() 씀. quick 알고리즘으로 안되네 ㅡㅡ

from collections import deque
import itertools, random

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

def quick_sort3(target_deque: deque, start_idx: int, end_idx: int):
    if start_idx >= end_idx:
        return

    pivot_idx = start_idx
    cur_start_idx = start_idx + 1
    cur_end_idx = end_idx

    while cur_start_idx != cur_end_idx:
        if target_deque[cur_start_idx] <= target_deque[pivot_idx]:
            cur_start_idx += 1
        else:
            while cur_start_idx != cur_end_idx:
                if target_deque[cur_end_idx] > target_deque[pivot_idx]:
                    cur_end_idx -= 1
                else:
                    target_deque[cur_start_idx], target_deque[cur_end_idx] = target_deque[cur_end_idx], target_deque[cur_start_idx]
                    cur_start_idx += 1
                    break
    if target_deque[cur_start_idx] <= target_deque[pivot_idx]:
        next_pivot_idx = cur_start_idx + 1
    else:
        next_pivot_idx = cur_start_idx

    pivot_value = target_deque[pivot_idx]
    target_idx = start_idx
    for target_value in itertools.islice(target_deque, start_idx + 1, next_pivot_idx):
        target_deque[target_idx] = target_value
        target_idx += 1
    target_deque[target_idx] = pivot_value
    next_pivot_idx = target_idx

    quick_sort3(target_deque, start_idx, next_pivot_idx - 1)
    quick_sort3(target_deque, next_pivot_idx + 1, end_idx)

def quick_selection(target_deque: deque, selected_idx: int, start_idx: int, end_idx: int):
    if start_idx >= end_idx:
        return

    #pivot_idx = start_idx
    pivot_idx = random.randint(selected_idx - 1 if selected_idx > start_idx else start_idx, selected_idx + 1 if selected_idx < end_idx else end_idx)
    #pivot_idx = random.randint(start_idx, end_idx)
    #cur_start_idx = start_idx + 1
    cur_start_idx = start_idx
    cur_end_idx = end_idx

    while cur_start_idx != cur_end_idx:
        if cur_start_idx == pivot_idx:
            cur_start_idx += 1
            continue
        if cur_end_idx == pivot_idx:
            cur_end_idx -= 1
            continue

        if target_deque[cur_start_idx] <= target_deque[pivot_idx]:
            cur_start_idx += 1
        else:
            while cur_start_idx != cur_end_idx:
                if target_deque[cur_end_idx] > target_deque[pivot_idx]:
                    cur_end_idx -= 1
                else:
                    target_deque[cur_start_idx], target_deque[cur_end_idx] = target_deque[cur_end_idx], target_deque[cur_start_idx]
                    cur_start_idx += 1
                    break
    if pivot_idx < cur_start_idx:
        if target_deque[cur_start_idx] <= target_deque[pivot_idx]:
            next_pivot_idx = cur_start_idx
        else:
            next_pivot_idx = cur_start_idx - 1
    elif pivot_idx > cur_start_idx:
        if target_deque[cur_start_idx] <= target_deque[pivot_idx]:
            next_pivot_idx = cur_start_idx + 1
        else:
            next_pivot_idx = cur_start_idx
    else:
        next_pivot_idx = pivot_idx
    target_deque[pivot_idx], target_deque[next_pivot_idx] = target_deque[next_pivot_idx], target_deque[pivot_idx]

    # 이 전까지는 quick_sort3() 와 동일

    if selected_idx == next_pivot_idx:
        return
    elif selected_idx < next_pivot_idx:
        quick_selection(target_deque, selected_idx, start_idx, next_pivot_idx - 1)
    else:
        quick_selection(target_deque, selected_idx, next_pivot_idx + 1, end_idx)


def solution():
    import sys
    sys.setrecursionlimit(5000000)
    input = sys.stdin.readline

    num_count, num_rank = map(int, input().split())
    num_deque = deque(map(int, input().split()))
    #num_count = 500000
    #num_rank = 3
    #num_deque = deque(range(num_count))
    #random.shuffle(num_deque)
    #reversed(num_deque)
    #print("Hello")

    #num_deque = quick_sort(num_deque)
    #quick_sort2(num_deque, 0, len(num_deque) - 1)
    #quick_sort3(num_deque, 0, len(num_deque) - 1)
    #quick_selection(num_deque, num_rank - 1, 0, len(num_deque) - 1)
    num_deque = sorted(num_deque)

    print(num_deque[num_rank - 1])


if __name__ == "__main__":
    solution()