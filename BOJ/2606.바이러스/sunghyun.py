count = 0
def dfs_recursive(graph, start, visited=[]):
    global count
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs_recursive(graph, i, visited)
            count += 1

count_of_computer = int(input())
count_of_pair = int(input())

graph = [[]*count_of_computer for _ in range(count_of_computer+1)]
for i in range(count_of_pair):
    node_a, node_b = map(int, input().split())
    graph[node_a].append(node_b)
    graph[node_b].append(node_a)

dfs_recursive(graph, 1, [0]*(count_of_computer+1))
print(count)
