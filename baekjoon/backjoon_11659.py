
# link: https://www.acmicpc.net/problem/11659
# 구간합 배열 연습문제
# sys.stdin.readline() 의 중요성. 속도측면.

def solution():
    num_count, cal_count = map(int, input().split(" "))
    #num_list = list(map(int, input().split(" ")))
    #
    #sum_list = [num_list[0]]
    #for target_idx, target_num in enumerate(num_list[1:]):
    #    sum_list.append(sum_list[target_idx] + target_num)
    sum_list = []
    for target_num in input().split(" "):
        if sum_list:
            sum_list.append(sum_list[-1] + int(target_num))
        else:
            sum_list.append(int(target_num))
        
    result_list = []
    for _ in range(cal_count):
        start_idx, end_idx = map(int, input().split(" "))
        if start_idx == 1:
            #print(sum_list[end_idx - 1])
            result_list.append(sum_list[end_idx - 1])
        else:
            #print(sum_list[end_idx - 1] - sum_list[start_idx - 2])
            result_list.append(sum_list[end_idx - 1] - sum_list[start_idx - 2])

    for target_result in result_list:
        print(target_result)

def solution_2nd():
    num_count, cal_count = map(int, input().split(" "))
    num_list = list(map(int, input().split(" ")))
    
    sum_list = [0]
    for target_num in num_list:
        sum_list.append(sum_list[-1] + target_num)

    result_list = []
    for _ in range(cal_count):
        start_idx, end_idx = map(int, input().split(" "))
        #print(sum_list[end_idx] - sum_list[start_idx - 1])
        result_list.append(sum_list[end_idx] - sum_list[start_idx - 1])
    
    for target_result in result_list:
        print(target_result)

def solution_3rd():
    import sys
    input = sys.stdin.readline

    num_count, cal_count = map(int, input().split())
    num_list = list(map(int, input().split()))

    sum_list = [0]
    for target_num in num_list:
        sum_list.append(sum_list[-1] + target_num)

    result_list = []
    for _ in range(cal_count):
        start_idx, end_idx = map(int, input().split())
        print(sum_list[end_idx] - sum_list[start_idx - 1])


if __name__ == "__main__":
    #print(solution())
    #solution()
    #solution_2nd()
    solution_3rd()