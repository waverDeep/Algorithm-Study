import sys
import heapq

N = int(input())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    elif x > 0:
        heapq.heappush(heap, (x, x))
    else:
        heapq.heappush(heap,(-x,x))
