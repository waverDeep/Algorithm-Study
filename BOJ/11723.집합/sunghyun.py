import sys

count = int(input())
S = set()
for i in range(count):
    line = sys.stdin.readline().split()
    if line[0] == 'all':
        S = set([i for i in range(1, 21)])
    elif line[0] == 'empty':
        S = set()
    elif line[0] == 'add':
        S.add(int(line[1]))
    elif line[0] == 'remove':
        S.discard(int(line[1]))
    elif line[0] == 'check':
        if int(line[1]) in S:
            print(1)
        else:
            print(0)
    elif line[0] == 'toggle':
        if int(line[1]) in S:
            S.discard(int(line[1]))
        else:
            S.add(int(line[1]))