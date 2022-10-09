
# link: https://www.acmicpc.net/problem/11003
# Level: P0
# 슬라이딩 윈도우. 큐 구조 센스 필요.
# python-dequq 이용
# 리스트[] 보다 튜플() 속도가 빠름

def solution():
    import sys
    input = sys.stdin.readline

    num_count, sub_length = map(int, input().split())
    num_list = list(map(int, input().split()))

    cur_start_idx = 0
    cur_end_idx = 0
    from collections import deque
    min_queue = deque()
    min_queue.append((0, num_list[0])) # [idx, value]
    result_list = [num_list[0]]
    while cur_end_idx + 1 < num_count:
        if cur_end_idx - cur_start_idx + 1 == sub_length:
            cur_start_idx += 1
            if min_queue[0][0] < cur_start_idx:
                min_queue.popleft()

        cur_end_idx += 1
        for queue_idx in reversed(range(len(min_queue))):
            if min_queue[queue_idx][1] > num_list[cur_end_idx]:
                min_queue.pop()
            else:
                break
        min_queue.append((cur_end_idx, num_list[cur_end_idx]))
        result_list.append(min_queue[0][1])                    

    print(*result_list)                



if __name__ == "__main__":
    solution()