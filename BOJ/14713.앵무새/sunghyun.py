n = int(input())
lines = []
for i in range(n):
    lines.append(list(map(str, input().split())))
target = list(map(str, input().split()))

for item in target:
    correct = False
    for idx in range(n):
        if len(lines[idx]) != 0:
            if item == lines[idx][0]:
                lines[idx].pop(0)
                correct = True
                break
    if not correct:
        break
left = 0
for line in lines:
    left += len(line)
if correct and left == 0:
    print("Possible")
else:
    print("Impossible")
