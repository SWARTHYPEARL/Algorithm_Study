
# link: https://www.acmicpc.net/problem/12891
# 슬라이딩 윈도우 개념 사용

def add_ACGT(input_char, list_ACGT):
    # add 1: the number of input char
    if input_char == "A":
        list_ACGT[0] += 1
    elif input_char == "C":
        list_ACGT[1] += 1
    elif input_char == "G":
        list_ACGT[2] += 1
    elif input_char == "T":
        list_ACGT[3] += 1

def sub_ACGT(input_char, list_ACGT):
    # subtract 1: the number of input char
    if input_char == "A":
        list_ACGT[0] -= 1
    elif input_char == "C":
        list_ACGT[1] -= 1
    elif input_char == "G":
        list_ACGT[2] -= 1
    elif input_char == "T":
        list_ACGT[3] -= 1

def solution():
    import sys
    input = sys.stdin.readline

    str_length, sub_length = map(int, input().split())
    str_DNA = list(input().rstrip())
    count_ACGT = list(map(int, input().split())) # min_A, min_C, min_G, min_T

    start_idx = 0
    end_idx = sub_length - 1
    for target_char in str_DNA[start_idx:end_idx + 1]:
        sub_ACGT(target_char, count_ACGT)

    pwd_count = 0
    while True:
        if all([i <= 0 for i in count_ACGT]):
            pwd_count += 1

        if end_idx < str_length - 1:
            add_ACGT(str_DNA[start_idx], count_ACGT)
            start_idx += 1

            end_idx += 1
            sub_ACGT(str_DNA[end_idx], count_ACGT)
        else:
            break
        
    print(pwd_count)

if __name__ == "__main__":
    solution()