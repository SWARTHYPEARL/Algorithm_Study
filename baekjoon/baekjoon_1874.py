
# link: https://www.acmicpc.net/problem/1874
# Level: S3
# 스택 문제

def solution():
    import sys
    input = sys.stdin.readline

    num_count = int(input())
    from collections import deque
    num_stack = deque()
    seq_num = 1
    result_list = []
    for _ in range(num_count):
        target_num = int(input())
        while True:
            if target_num >= seq_num:
                num_stack.append(seq_num)
                result_list.append("+")
                seq_num += 1
            elif not num_stack:
                print("NO")
                return
            elif target_num == num_stack[-1]:
                num_stack.pop()
                result_list.append("-")
                break
            else:
                num_stack.pop()
                result_list.append("-")

    for target_result in result_list:
        print(target_result)




if __name__ == "__main__":
    solution()