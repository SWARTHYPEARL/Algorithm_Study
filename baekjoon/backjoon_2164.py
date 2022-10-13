
# link: https://www.acmicpc.net/problem/2164
# Level: S4
# 스택 기본 문제. 그러나 짝-홀 관계로 풀 수 있을 것 같기도?

def solution():
    total_num = int(input())
    result_num = 1
    while total_num != 1:
        total_num = total_num // 2
        result_num *= 2
        
    print(result_num)

def solution_2nd():
    total_num = int(input())
    from collections import deque
    card_deque = deque()

    for i in range(1, total_num + 1):
        card_deque.append(i)
    while len(card_deque) > 1:
        card_deque.popleft()
        card_deque.append(card_deque.popleft())

    print(card_deque[0])


if __name__ == "__main__":
    #solution()
    solution_2nd()