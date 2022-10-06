
# Link: https://school.programmers.co.kr/learn/courses/30/lessons/43163


def generate_graph(words):
    node = [0] * len(words)
    graph = []
    for _ in range(len(words)):
        graph.append(node.copy())

    for node_idx, connection_list in enumerate(graph):
        cmp_word_list = list(words[node_idx])
        
        for word_idx, target_word in enumerate(words):
            unpaired_count = 0
            for letter_idx, target_letter in enumerate(list(target_word)):
                if target_letter != cmp_word_list[letter_idx]:
                    unpaired_count += 1
            
            if unpaired_count <= 1:
                graph[node_idx][word_idx] = 1

    return graph
        
def DFS(graph, v, visited, depth):
    depth += 1
    visited[v] = depth

    for node_idx, node in enumerate(graph[v]):
        if node == 1 and (visited[node_idx] == -1 or visited[node_idx] > depth):
            DFS(graph, node_idx, visited, depth)
    

def solution(begin, target, words):
    # no solution
    if target not in words:
        return 0

    words.insert(0, begin)
    graph = generate_graph(words)
    visited = [-1] * len(words)
    DFS(graph, 0, visited, -1)
    
    answer = visited[words.index(target)]

    return answer

if __name__ == "__main__":

    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))