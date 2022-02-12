# 걷거나 순간이동을 할 수 있음
from collections import deque


def bfs(distance, N, K):
    need_visited = deque()
    need_visited.append(N)

    while need_visited:
        step = need_visited.popleft()
        if step == K:
            print(distance[step])
            break
        route = [step - 1, step + 1, step * 2]
        for move_step in route:
            if 0 <= move_step < len(distance) and distance[move_step] == 0:
                distance[move_step] = distance[step] + 1
                need_visited.append(move_step)


N, K = map(int, input().split())
distance = [0] * (100001)
bfs(distance, N, K)