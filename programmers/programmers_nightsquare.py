
# Link: https://school.programmers.co.kr/learn/courses/30/lessons/12927


def solution(n, works):
    #no night works
    if sum(works) <= n:
        return 0

    # descend sort
    works.sort(reverse=True)

    while n > 0:
        target_work = works[0]

        target_idx = 0
        while True:
            if n > 0 and works[target_idx] == target_work:
                works[target_idx] -= 1
                n -= 1

                target_idx += 1
            else:
                break

    answer = sum([i * i for i in works])

    return answer





if __name__ == "__main__":

    print(solution(4, [4, 3, 3]))