
# link: https://www.acmicpc.net/problem/1940

def solution():
    num_count = int(input())
    final_num = int(input())

    import sys
    num_list = list(map(int, sys.stdin.readline().split()))
    pair_dict = {}
    pair_count = 0
    for target_num in num_list:
        if target_num >= final_num:
            continue

        if final_num - target_num in pair_dict:
            pair_count += 1
            del pair_dict[final_num - target_num]
        else:
            pair_dict[target_num] = None

    print(pair_count)

if __name__ == "__main__":
    solution()