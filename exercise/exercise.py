

def display_2d(target_list):
    for target_row in target_list:
        print(target_row)

if __name__ == "__main__":

    tmp_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #display_2d(list(map(list, zip(*tmp_list))))
    from collections import Counter
    from collections import deque

    tmp_deque = deque(maxlen=3)
    tmp_deque.append(1)
    tmp_deque.append(2)
    tmp_deque.append(3)
    tmp_deque.appendleft(4)

    print(tmp_deque)