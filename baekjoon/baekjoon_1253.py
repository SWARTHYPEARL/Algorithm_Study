
# link: https://www.acmicpc.net/problem/1253
# 정렬 & 투포인터 문제.
# 투포인터 및 인덱스 히스토리를 사용해서 접근
# 은 잘못된 접근. 음수가 포함되었음을 고려.

def solution():
    import sys
    input = sys.stdin.readline

    num_count = int(input())
    num_list = list(map(int, input().split()))
    if num_count <= 1:
        print(0)
        return

    num_list.sort()
    
    start_idx = 0
    end_idx = 1
    sum_pointer = 1
    good_count = 0
    while sum_pointer < len(num_list) and end_idx < len(num_list):
        target_sum = num_list[start_idx] + num_list[end_idx]
        
        while sum_pointer < len(num_list):
            cmp_sum = num_list[sum_pointer]
            if target_sum > cmp_sum:
                sum_pointer += 1
            elif target_sum == cmp_sum:
                good_count += 1
                break
            else:
                break
        
        if end_idx == start_idx + 1:
            end_idx += 1
        else:
            if end_idx + 1 < len(num_list) and num_list[end_idx + 1] - num_list[end_idx] <= num_list[start_idx + 1] - num_list[start_idx]:
                end_idx += 1
            else:
                start_idx += 1

    print(good_count)
        
def solution2():
    import sys, heapq
    from collections import deque
    input = sys.stdin.readline

    num_count = int(input())
    num_list = list(map(int, input().split()))
    heapq.heapify(num_list)

    acc_num_list = []
    acc_num_list.append(heapq.heappop(num_list))
    acc_num_list.append(heapq.heappop(num_list))

    good_count = 0
    cur_upper_idx = 1
    cur_lower_idx = 0
    while len(num_list) != 0:
        target_num = heapq.heappop(num_list)
        before_indexes = deque([(0, 0)], maxlen=2)
        while before_indexes[0] != (cur_upper_idx, cur_lower_idx):
            if target_num == (acc_num_list[cur_upper_idx] + acc_num_list[cur_lower_idx]):
                good_count += 1
                break
            before_indexes.append((cur_upper_idx, cur_lower_idx))

            # 다른 두 수의 합이 대상보다 작은 경우
            if target_num > (acc_num_list[cur_upper_idx] + acc_num_list[cur_lower_idx]):
                # 다른 두 수의 indexes 증가 가능한 경우
                if cur_upper_idx < len(acc_num_list) - 1 and cur_lower_idx < cur_upper_idx - 1:
                    if acc_num_list[cur_upper_idx + 1] - acc_num_list[cur_upper_idx] < acc_num_list[cur_lower_idx + 1] - acc_num_list[cur_lower_idx]:
                        cur_upper_idx += 1
                    else:
                        cur_lower_idx += 1

                # upper_idx만 증가 가능한 경우
                elif cur_upper_idx < len(acc_num_list) - 1:
                    cur_upper_idx += 1

                # lower_idx만 증가 가능한 경우
                elif cur_lower_idx < cur_upper_idx - 1:
                    cur_lower_idx += 1

                # indexes 증가 불가능한 경우
                else:
                    break

            # 다른 두 수의 합이 대상보다 큰 경우
            elif target_num < (acc_num_list[cur_upper_idx] + acc_num_list[cur_lower_idx]):
                # 다른 두 수의 indexes 감소 가능한 경우
                if cur_upper_idx > cur_lower_idx + 1 and cur_lower_idx > 0:
                    if acc_num_list[cur_upper_idx] - acc_num_list[cur_upper_idx - 1] < acc_num_list[cur_lower_idx] - acc_num_list[cur_lower_idx - 1]:
                        cur_upper_idx -= 1
                    else:
                        cur_lower_idx -= 1

                # upper_idx만 감소 가능한 경우
                elif cur_upper_idx > cur_lower_idx + 1:
                    cur_upper_idx -= 1

                # lower_idx만 감소 가능한 경우
                elif cur_lower_idx > 0:
                    cur_lower_idx -= 1

                # indexes 감소 불가능한 경우
                else:
                    break

        acc_num_list.append(target_num)

    print(good_count)

def solution3():
    import sys
    input = sys.stdin.readline

    num_count = int(input())
    num_list = list(map(int, input().split()))

    num_list.sort()

    good_count = 0
    for target_idx, target_num in enumerate(num_list):
        cur_upper_idx = num_count - 1
        cur_lower_idx = 0
        while cur_upper_idx > cur_lower_idx:
            if target_idx != cur_upper_idx and target_idx != cur_lower_idx:
                if target_num == num_list[cur_upper_idx] + num_list[cur_lower_idx]:
                    good_count += 1
                    break

                elif target_num > num_list[cur_upper_idx] + num_list[cur_lower_idx]:
                    cur_lower_idx += 1
                else:
                    cur_upper_idx -= 1

            elif target_idx == cur_upper_idx:
                cur_upper_idx -= 1
            elif target_idx == cur_lower_idx:
                cur_lower_idx += 1
            else:
                break

    print(good_count)


if __name__ == "__main__":
    #solution()
    #solution2()
    solution3()