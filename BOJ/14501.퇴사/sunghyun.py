N = int(input())
T = []
P = []
dp_table = []
for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    dp_table.append(p)
dp_table.append(0)
for i in range(N-1, -1, -1):
    if T[i] + i > N:
        dp_table[i] = dp_table[i + 1]
    else:
        dp_table[i] = max(dp_table[i+1], P[i] + dp_table[i+T[i]])
print(dp_table[0])