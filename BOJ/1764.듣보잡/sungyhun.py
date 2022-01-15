n, m = map(int, input().split())
d_names = {}
for idx in range(n+m):
    name = input()
    if name in d_names:
        d_names[name] += 1
    else:
        d_names[name] = 1
dbj = [key for key, value in d_names.items() if value == 2]
dbj.sort()
print(len(dbj))
for name in dbj:
    print(name)