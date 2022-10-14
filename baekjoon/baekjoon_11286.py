
# link: https://www.acmicpc.net/problem/11286
# Level: S1
# 우선순위큐 구현. 시험에서는 그냥 import heapq 로 때우자

def heap_criteria(num_A: int, num_B: int):
    # return True: num_A meet criteria
    # return False: num_B meet criteria

    # criteria: abs min
    if abs(num_A) < abs(num_B):
        return True
    elif abs(num_A) == abs(num_B):
        if num_A < num_B:
            return True
        else:
            return False
    else:
        return False

def heap_pop(target_heap: list):
    if len(target_heap) == 1:
        return 0
    elif len(target_heap) == 2:
        pop_value = target_heap[1]
        del target_heap[1]
        return pop_value

    pop_value = target_heap[1]
    target_heap[1] = target_heap[-1]
    del target_heap[-1]

    target_idx = 1
    cmp_idx = 1
    while len(target_heap) > target_idx * 2:
        if len(target_heap) > target_idx * 2 + 1 and not heap_criteria(target_heap[target_idx * 2], target_heap[target_idx * 2 + 1]):
            cmp_idx = target_idx * 2 + 1
        else:
            cmp_idx = target_idx * 2

        if heap_criteria(target_heap[target_idx], target_heap[cmp_idx]):
            break

        target_heap[target_idx], target_heap[cmp_idx] = target_heap[cmp_idx], target_heap[target_idx]
        target_idx = cmp_idx

    return pop_value

def heap_add(target_heap: list, target_element: int):
    target_heap.append(target_element)

    target_idx = len(target_heap) - 1
    while target_idx != 1:
        if not heap_criteria(target_heap[target_idx // 2], target_heap[target_idx]):
            target_heap[target_idx // 2], target_heap[target_idx] = target_heap[target_idx], target_heap[target_idx // 2]
            target_idx = target_idx // 2
        else:
            break


def solution():
    import sys
    input = sys.stdin.readline

    num_count = int(input())

    abs_min_heap = [0]
    for _ in range(num_count):
        target_num = int(input())

        if target_num == 0:
            print(heap_pop(abs_min_heap))
        else:
            heap_add(abs_min_heap, target_num)



if __name__ == "__main__":
    solution()