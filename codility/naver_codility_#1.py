# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def simple_factorial(n):
    if n > 1:
        return n * simple_factorial(n - 1)
    else:
        return 1

def solution(S):
    # write your code in Python 3.6
    
    N = len(S)
    a_count = S.count("a")

    # no solution
    if a_count % 3 != 0:
        return 0
    
    # split position of "a"
    a_split_1 = 0
    a_split_2 = 0

    # the number of "a" to split
    a_split_count = a_count / 3
    a_stack = 0

    a_start_idx = 0
    a_find_idx = 0

    # start searching a-position
    a_find_idx = S.find("a", a_find_idx)
    # no letter "a" solution: nCr (Combination)
    if a_find_idx <= -1:
        return int(simple_factorial(N - 1) / (simple_factorial(N - 1 - 2) * simple_factorial(2)))
    a_stack += 1

    # start loop with first a-position
    while True:
        if a_stack == a_split_count:
            a_start_idx = a_find_idx
            a_find_idx = a_find_idx + len("a")
            a_find_idx = S.find("a", a_find_idx)

            if a_split_1 == 0:
                a_split_1 = a_find_idx - a_start_idx
            else:
                a_split_2 = a_find_idx - a_start_idx
                break

            a_stack = 1

        else:
            a_find_idx = a_find_idx + len("a")
            a_find_idx = S.find("a", a_find_idx)
            a_stack += 1

    return a_split_1 * a_split_2
    





if __name__ == "__main__":

    #tmp = "abaa"
    #print(tmp.find("a", 3))
    print(solution("aaabababbabbabaa"))
