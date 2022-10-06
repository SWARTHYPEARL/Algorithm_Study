
# link: https://school.programmers.co.kr/learn/courses/30/lessons/42628

def solution(operations):

    total_length = 0
    heap_list_max = [0]
    heap_list_min = [0]
    for target_op in operations:
        op_ID, op_num = target_op.split(" ")
        op_num = int(op_num)

        print(f"\n\nop_ID: {op_ID}")
        print(f"op_num: {op_num}")
        print(f"total_length: {total_length}")
        print(f"heap_list_max: {heap_list_max}")
        print(f"heap_list_min: {heap_list_min}")
        if op_ID == "I":
            heap_list_max.append(op_num)
            heap_list_min.append(op_num)
            total_length += 1
            if total_length == 1:
                continue

            # heapsort for max root
            max_target_idx = len(heap_list_max) - 1
            while True:
                max_parent_idx = int(max_target_idx / 2)
                if heap_list_max[max_parent_idx] < heap_list_max[max_target_idx]:
                    heap_list_max[max_parent_idx], heap_list_max[max_target_idx] =  heap_list_max[max_target_idx], heap_list_max[max_parent_idx]
                    max_target_idx = max_parent_idx
                else:
                    break
                
                if max_target_idx == 1:
                    break
            
            # heapsort for min root
            min_target_idx = len(heap_list_min) - 1
            while True:
                min_parent_idx = int(min_target_idx / 2)
                if heap_list_min[min_parent_idx] > heap_list_min[min_target_idx]:
                    heap_list_min[min_parent_idx], heap_list_min[min_target_idx] =  heap_list_min[min_target_idx], heap_list_min[min_parent_idx]
                    min_target_idx = min_parent_idx
                else:
                    break
                
                if min_parent_idx == 1:
                    break

        elif op_ID == "D":
            if total_length == 0:
                continue
            elif total_length == 1:
                total_length = 0
                heap_list_max = [0]
                heap_list_min = [0]
                continue

            if op_num == 1:
                # delete max value
                del heap_list_max[1]
                total_length -= 1
                
                max_target_idx = 1
                while True:
                    # left child check
                    max_leftchild_idx = max_target_idx * 2
                    if len(heap_list_max) > max_leftchild_idx:
                        if heap_list_max[max_target_idx] < heap_list_max[max_leftchild_idx]:
                            heap_list_max[max_target_idx], heap_list_max[max_leftchild_idx] = heap_list_max[max_leftchild_idx], heap_list_max[max_target_idx]
                            max_target_idx = max_leftchild_idx
                            continue

                    # right child check
                    max_rightchild_idx = max_target_idx * 2 + 1
                    if len(heap_list_max) > max_rightchild_idx:
                        if heap_list_max[max_target_idx] < heap_list_max[max_rightchild_idx]:
                            heap_list_max[max_target_idx], heap_list_max[max_rightchild_idx] = heap_list_max[max_rightchild_idx], heap_list_max[max_target_idx]
                            max_target_idx = max_rightchild_idx
                            continue
                    
                    # swap exit
                    break
                
            elif op_num == -1:
                # delete min value
                del heap_list_min[1]
                total_length -= 1
                
                min_target_idx = 1
                while True:
                    # left child check
                    min_leftchild_idx = min_target_idx * 2
                    if len(heap_list_min) > min_leftchild_idx:
                        if heap_list_min[min_target_idx] > heap_list_min[min_leftchild_idx]:
                            heap_list_min[min_target_idx], heap_list_min[min_leftchild_idx] = heap_list_min[min_leftchild_idx], heap_list_min[min_target_idx]
                            min_target_idx = min_leftchild_idx
                            continue

                    # right child check
                    min_rightchild_idx = min_target_idx * 2 + 1
                    if len(heap_list_min) > min_rightchild_idx:
                        if heap_list_min[min_target_idx] > heap_list_min[min_rightchild_idx]:
                            heap_list_min[min_target_idx], heap_list_min[min_rightchild_idx] = heap_list_min[min_rightchild_idx], heap_list_min[min_target_idx]
                            min_target_idx = min_rightchild_idx
                            continue
                    
                    # swap exit
                    break

            else:
                exit(1)
        else:
            exit(1)

    if total_length == 0:
        answer = [0, 0]
    elif total_length == 1:
        if len(heap_list_max) > len(heap_list_min):
            target_heap_list = heap_list_max
            cmp_heap_list = heap_list_min
        else:
            target_heap_list = heap_list_min
            cmp_heap_list = heap_list_max
        for target_idx in range(1, len(target_heap_list)):
            if target_heap_list[target_idx] in cmp_heap_list[1:]:
                answer = [target_heap_list[target_idx], target_heap_list[target_idx]]
                break

    else:
        answer = [heap_list_max[1], heap_list_min[1]]

    #answer = []
    return answer


if __name__ == "__main__":
    #print("Hello")
    #print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "D -1"]))
