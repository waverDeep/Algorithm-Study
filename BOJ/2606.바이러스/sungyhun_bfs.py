count = 0


def bfs(graph, start, count_of_computer):
    global count
    need_visited = []
    visited = []
    need_visited.append(start)
    while need_visited:
        node = need_visited.pop(0)
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
            count += 1
    return visited


count_of_computer = int(input())
count_of_pair = int(input())


graph = [[] * count_of_computer for _ in range(count_of_computer + 1)]
for i in range(count_of_pair):
    node_a, node_b = map(int, input().split())
    graph[node_a].append(node_b)
    graph[node_b].append(node_a)

bfs(graph, 1, count_of_computer)
print(count - 1)