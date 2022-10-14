
# link: https://www.acmicpc.net/problem/2023
# Level: G5
# DFS 응용

import math

def is_prime(value: int):
    #for target_num in range(2, value // 2 + 1):
    for target_num in range(2, round(math.sqrt(value)) + 1):
        if value % target_num == 0:
            return False
    return True

def solution():
    import sys
    input = sys.stdin.readline

    digit_size = int(input())

    digit_node = [1, 3, 5, 7, 9]
    prime_list = []

    def DFS(value: int):
        if len(str(value)) == digit_size:
            prime_list.append(value)
        else:
            for target_digit in digit_node:
                target_value = int(str(value) + str(target_digit))
                if is_prime(target_value) is True:
                    DFS(target_value)

    first_digit_node = [2, 3, 5, 7]
    for target_first_digit in first_digit_node:
        DFS(target_first_digit)

    for target_prime in prime_list:
        print(target_prime)

if __name__ == "__main__":
    solution()