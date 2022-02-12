from collections import deque

dx=[1,2,1,2,-1,-2,-1,-2]
dy=[2,1,-2,-1,2,1,-2,-1]

def bfs(x,y):
    cnt = 0
    queue = deque([(x,y,cnt)])
    while queue:
        x, y, cnt = queue.popleft()
        visited[x][y] = 1
        if x == end[0] and y == end[1]:
            return cnt
        cnt += 1 # cnt의 위치도 중요하지 queue에 append 될 때마다 cnt가 증가하는게 아니니까
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if visited[nx][ny] == 0:
                queue.append((nx,ny, cnt))
                visited[nx][ny] = 1 # 방문처리를 해주지 않아서 두번째 테스트 케이스가 무한루프돌았음
        
T =  int(input())
for _ in range(T):
    l = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    visited = [[0 for _ in range(l)] for _ in range(l)]
    print(bfs(start[0], start[1]))
