
# Link: https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):

    import copy
    triangle_stack = copy.deepcopy(triangle)

    for row_idx, target_row in enumerate(triangle):
        # skip first row
        if row_idx == 0:
            continue

        for elmt_idx, target_elmt in enumerate(target_row):
            if elmt_idx == len(target_row) - 1:
                continue

            if triangle_stack[row_idx][elmt_idx] < triangle_stack[row_idx - 1][elmt_idx] + triangle[row_idx][elmt_idx]:
                triangle_stack[row_idx][elmt_idx] = triangle_stack[row_idx - 1][elmt_idx] + triangle[row_idx][elmt_idx]
            if len(target_row) > elmt_idx + 1 and triangle_stack[row_idx][elmt_idx + 1] < triangle_stack[row_idx - 1][elmt_idx] + triangle[row_idx][elmt_idx + 1]:
                triangle_stack[row_idx][elmt_idx + 1] = triangle_stack[row_idx - 1][elmt_idx] + triangle[row_idx][elmt_idx + 1]

    answer = max(triangle_stack[-1])

    return answer


if __name__ == "__main__":

    triangle_list = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(triangle_list))