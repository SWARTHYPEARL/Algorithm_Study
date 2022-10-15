
# link: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo
# Level: 모의 SW 역량테스트

def solution():
    import sys
    input = sys.stdin.readline

    num_count, top_K = map(int, input().split())
    num_list = list(input().rstrip())

    split_num = num_count // 4
    print(num_list[0:split_num])
    print(int("0x" + ''.join(num_list[split_num + 1:split_num + 4]), 16))



if __name__ == "__main__":
    solution()