
# link: https://www.acmicpc.net/problem/11399
# Level: S4
# 삽입정렬 구현: 오름차순

def solution():
    import sys
    input = sys.stdin.readline

    person_count = int(input())
    time_list = list(map(int, input().split()))

    for target_idx in range(1, person_count):
        for cmp_idx, cmp_value in enumerate(time_list[:target_idx]):
            if cmp_value > time_list[target_idx]:
                target_value = time_list[target_idx]
                del time_list[target_idx]
                time_list.insert(cmp_idx, target_value)

    total_time = 0
    for target_idx, target_value in enumerate(time_list):
        total_time += target_value * (len(time_list) - target_idx)
    print(total_time)


if __name__ == "__main__":
    solution()