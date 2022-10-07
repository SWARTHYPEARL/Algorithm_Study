
# link: https://www.acmicpc.net/problem/2018
# 리스트 투포인트 알고리즘

def solution():
    target_num = int(input())
    if target_num == 1:
        print(1)
        return
    
    target_limit = target_num // 2 + target_num % 2
    start_num = 1
    end_num = 1
    seq_sum = 1
    seq_count = 1
    while True:
        if seq_sum < target_num:
            end_num += 1
            if end_num > target_limit:
                break

            seq_sum += end_num
        elif seq_sum > target_num:
            seq_sum -= start_num
            start_num += 1

        if seq_sum == target_num:
            seq_count += 1

            seq_sum -= start_num
            start_num += 1

    print(seq_count)

if __name__ == "__main__":
    solution()