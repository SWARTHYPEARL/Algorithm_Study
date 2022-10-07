
# link: https://www.acmicpc.net/problem/1546
# map() 및 python list의 적절한 활용

def solution():
    num_count = int(input())
    #num_list = input().split(" ")
    #score_list = [int(i) for i in num_list]
    score_list = list(map(int, input().split(" ")))

    score_max = max(score_list)
    #total_score = 0
    #for target_score in score_list:
    #    total_score += target_score / score_max * 100
        
    #return total_score / num_count
    return sum(score_list) / score_max * 100 / int(num_count)


if __name__ == "__main__":
    print(solution())