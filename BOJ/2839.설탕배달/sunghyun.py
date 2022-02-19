N = int(input())
count = 0
while N > 0:
    if N % 5 == 0:
        temp = int(N / 5)
        N -= 5 * temp
        count += temp
        break
    N -= 3
    count += 1
if N == 0:
    print(count)
else:
    print(-1)