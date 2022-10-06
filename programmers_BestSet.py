

def solution(n, s):
    if n > s:
        return [-1]

    sn_ratio = s / n
    answer = [int(sn_ratio)] * n
    for ans_idx in range(s - sum(answer)):
        answer[(len(answer) - 1) - ans_idx] += 1

    return answer

    answer = []

    sn_ratio = s / n
    for ratio_mul in range(1, n + 1):
        target_num = int(sn_ratio)
        if abs(ratio_mul * sn_ratio - (sum(answer) + target_num)) > abs(ratio_mul * sn_ratio - (sum(answer) + target_num + 1)):
            answer.append(target_num + 1)
        else:
            answer.insert(0, target_num)
            


    return answer



if __name__ == "__main__":

    ans = solution(1000, 11531215)
    print(f"answer: {ans}")
    print(f"answer: {sum(ans)}")