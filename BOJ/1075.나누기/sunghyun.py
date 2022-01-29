N = int(input())
F = int(input())

N_small = int(N / 100) * 100
count = 0
while True:
    if (N_small+count) % F == 0:
        break
    count += 1
print(str(count).zfill(2))