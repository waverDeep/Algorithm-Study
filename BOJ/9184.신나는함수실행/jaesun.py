# d = [[[0]*101 for _ in range(102)] for _ in range(102)]
# 0보다 작으면 1 리턴해주고 20보다 크면 w(20,20,20)이기에 d 범위 클 필요 없다.
d = [[[0]*21 for _ in range(21)] for _ in range(21)]


def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    # 이 위치도 중요 맨위에 놔버리면 20보다 클 때나 0보다 작을 때 index 에러 뱉겠지
    if d[a][b][c] != 0:
        return d[a][b][c]
    # 메모이제이션
    if a < b and b < c:
        d[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return d[a][b][c]
    d[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return d[a][b][c]

    


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
    print("w(%d, %d, %d) = %d"%(a,b,c,w(a,b,c)))


    