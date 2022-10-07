
# link: https://www.acmicpc.net/problem/11720

def solution():
    num_count = int(input())
    num_list = list(input()) # split string into char one by one
    return(sum([int(i) for i in num_list])) # sum all elements in the list


if __name__ == "__main__":
    print(solution())