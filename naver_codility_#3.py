def solution(A, K):
    # n: number of nails
    # K: number of hammering

    n = len(A)
    best = 0
    count = 1
    for i in range(n - K - 1):
        if (A[i] == A[i + 1]):
            count = count + 1
        else:
            #count = 0
            count = 1
        best = max(best, count)
    #result = best + 1 + K
    result = best + K

    #return result
    return result if result <= n else n


if __name__ == "__main__":

    print(solution([1, 1, 3, 3, 3, 4, 5, 5, 5, 5], 13))