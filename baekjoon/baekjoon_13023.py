
# link: https://www.acmicpc.net/problem/13023
# Level: G5
# DFS 응용. 전역변수 특징을 잘 파악해야함.

def solution():
    import sys
    input = sys.stdin.readline

    person_count, relation_count = map(int, input().split())
    relation_list = [[] for _ in range(person_count)]
    visited_list = [False] * person_count
    for _ in range(relation_count):
        person_A, person_B = map(int, input().split())
        relation_list[person_A].append(person_B)
        relation_list[person_B].append(person_A)

    is_depth_5 = False
    def DFS(cur_node: int, cur_depth: int, cur_visited_list: list):
        cur_visited_list[cur_node] = True
        cur_depth += 1
        if cur_depth == 5:
            is_depth_5 = True
            print(1)
            exit(0)
        else:
            for next_person in relation_list[cur_node]:
                if cur_visited_list[next_person] is False:
                    DFS(next_person, cur_depth, cur_visited_list)

        cur_visited_list[cur_node] = False

    for target_person in range(person_count):
        DFS(target_person, 0, visited_list)
    print(0)


if __name__ == "__main__":
    solution()