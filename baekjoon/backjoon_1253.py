
# link: https://www.acmicpc.net/problem/1253
# 정렬 & 투포인터 문제.
# 미해결: sum_pointer를 갱신하면서 포인터를 처음으로 초기화해야함.

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
        
        

if __name__ == "__main__":
    solution()