def find_parent(x):
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    x, y = find_parent(x), find_parent(y)
    parent[x] = y


n = int(input())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(m)]
arr = sorted(arr, key=lambda k: k[2])
parent = [i for i in range(0, n + 2)]
answer = 0
for a in arr:
    start, end, weight = a
    # cycle 확인
    if find_parent(start) == find_parent(end):
        continue
    else:
        answer += weight
        union_parent(start, end)
print(answer)
