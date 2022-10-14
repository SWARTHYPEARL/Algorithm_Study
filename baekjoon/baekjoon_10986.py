
# link: https://www.acmicpc.net/problem/10986
# 나머지 특성을 이용한 부분합

def solution():
    import sys
    input = sys.stdin.readline

    num_count, num_divide = map(int, input().split())

    remain_table = [0]
    remain_dict = {}
    for target_idx, target_num in enumerate(list(map(int, input().split()))):
        target_remain = (remain_table[target_idx] + target_num) % num_divide
        remain_table.append(target_remain)
        if target_remain in remain_dict:
            remain_dict[target_remain] += 1
        else:
            remain_dict[target_remain] = 1
    #print(remain_table)

    result_count = remain_dict[0] if 0 in remain_dict else 0
    for target_remain_count in remain_dict.values():
        result_count += int(target_remain_count * (target_remain_count - 1) / 2)

    print(result_count)


if __name__ == "__main__":
    solution()