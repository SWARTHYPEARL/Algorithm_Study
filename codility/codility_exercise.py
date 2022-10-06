def solution(A):
    # write your code in Python 3.6
    
    result = {}
    for target_elmt in A:
        if target_elmt in result.keys():
            del result[target_elmt]
        else:
            result[target_elmt] = None
    
    return list(result.keys())[0]

if __name__ == "__main__":

    print(solution([9, 3, 9, 3, 9, 7, 9]))