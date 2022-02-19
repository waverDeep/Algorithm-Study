T = int(input())

d = [0] * 101

d[1] = 1
d[2] = 1
d[3] = 1

for _ in range(T):
    N = int(input())
    for i in range(4, N+1):
        d[i] = d[i-2] + d[i-3]
    print(d[N])

# 점화식을 구하고 바텀업 방식으로 구현(9184는 점화식 자체에 재귀가 있다)

# 먼저 dp 테이블 만들어놓고 시작
# d= [0] * 101
# for i in range(4,101):
#     d[i] = d[i-2] + d[i-3]

# for _ in range(T):
#     N = int(input())
#     print(d(N))
