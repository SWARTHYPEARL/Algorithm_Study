
# link: https://www.acmicpc.ne1t/problem/17298
# Level: G4
# 스택의 특성을 이용한 센스

def solution():
    import sys
    input = sys.stdin.readline

    seq_size = int(input())
    seq_list = tuple(map(int, input().split()))

    from collections import deque
    seq_stack = deque()
    output_stack = deque()
    for target_idx, target_num in enumerate(seq_list):
        while seq_stack and seq_stack[-1][1] < target_num:
            pop_idx = seq_stack.pop()[0]
            output_stack[pop_idx] = target_num

        seq_stack.append((target_idx, target_num))
        output_stack.append(-1)
                
    print(*output_stack)

def solution_2nd():
    import sys
    input = sys.stdin.readline
    seq_size = int(input())
    seq_list = tuple(map(int, input().split()))

    from collections import deque
    seq_stack = deque()
    output_list = [-1] * seq_size
    for target_idx, target_num in enumerate(seq_list):
        while seq_stack and seq_stack[-1][1] < target_num:
            pop_idx = seq_stack.pop()[0]
            output_list[pop_idx] = target_num
            
        seq_stack.append((target_idx, target_num))
                
    print(*output_list)


if __name__ == "__main__":
    #solution()
    solution_2nd()