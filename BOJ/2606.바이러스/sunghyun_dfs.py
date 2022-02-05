count = 0
def dfs_recursive(graph, start, visited=[]):
    global count
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs_recursive(graph, i, visited)
            count += 1

# 컴퓨터의 대수 입력
count_of_computer = int(input())
# 쌍의 개수 입력
count_of_pair = int(input())

# 그래프를 저장할 공간 만들어놓기 1번컴퓨터부터 존재해서 0번 버리고 1번 배열부터 컴퓨터의 대수까지 배열 만들기
graph = [[]*count_of_computer for _ in range(count_of_computer+1)]
# 그래프 만들기
for i in range(count_of_pair):
    node_a, node_b = map(int, input().split())
    graph[node_a].append(node_b)
    graph[node_b].append(node_a)

# 재귀함수로 연결된 노드 방문하기
dfs_recursive(graph, 1, [0]*(count_of_computer+1))
print(count)
