# 가운데를 말해요
import sys
import heapq

N = int(input())
heap1 = []
heap2 = []

for i in range(N):
    x = int(sys.stdin.readline().rstrip())
    if i % 2 == 0:
        if heap2 and x > heap2[0]:
            heapq.heappush(heap1, -heapq.heappop(heap2))
            heapq.heappush(heap2, x)
        else:
            heapq.heappush(heap1, -x)
    else:
        if x < -heap1[0]:
            heapq.heappush(heap2,-heapq.heappop(heap1))
            heapq.heappush(heap1, -x)
        else:
            heapq.heappush(heap2, x)
    print(-heap1[0])