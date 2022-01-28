n = int(input())
guys = []

for i in range(n):
    weight, tall = map(int, input().split())
    guys.append([weight, tall])

count = 1
for i in range(len(guys)):
    for j in range(len(guys)):
        if guys[i][0] < guys[j][0] and guys[i][1] < guys[j][1]:
            count += 1
    print(count)
    count = 1