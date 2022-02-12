from collections import deque

N, K = map(int, input().split())
visited = [-1]*100001

def bfs(x):
    queue = deque([x])
    visited[x] = 0
    while queue:
        x = queue.popleft()
        if x == K:
            print(visited[x])
            break
        for nx in (x+1, x-1, 2*x):  # 이 기법 잘 사용하기!!
            if nx >= 0 and nx <= 100000 and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                queue.append(nx)

bfs(N)

def bfs2(x):
    queue = deque([x])
    visited[x] = 0
    while queue:
        x = queue.popleft()
        for nx in (x+1, x-1, 2*x):  # 이 기법 잘 사용하기!!
            if nx >= 0 and nx <= 100000 and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                if nx == K:
                    print(visited[nx])
                    exit(0)
                queue.append(nx)

# bfs2(N) -> 틀렸습니다. 같은 위치에 있을 때 값이 나오지 않는다. 
            

