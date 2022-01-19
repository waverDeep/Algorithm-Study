import operator
import sys

n, m = map(int, input().split()) # 수강가능인원, 클릭 횟수
clicks = {}
for idx in range(m):
    hak = sys.stdin.readline().rstrip()
    clicks[hak] = idx
clicks = sorted(clicks.items(), key=operator.itemgetter(1))
if n > len(clicks):
    n = len(clicks)
for idx in range(n):
    print(clicks[idx][0])