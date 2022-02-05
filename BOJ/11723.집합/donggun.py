m = int(input())

# act = []
s = [0] * 20

# for i in range(m):
#     act.append(input().split())
#
# for idx, a in enumerate(act):
for i in range(m):
    a = input().split()
    if a[0] == "add":
        s[int(a[1])] = 1

    elif a[0] == "remove":
        s[int(a[1])] = 0

    elif a[0] == "check":
        print(s[int(a[1])])

    elif a[0] == "toggle":
        s[int(a[1])] = abs(s[int(a[1])] - 1)

    elif a[0] == "all":
        for i in range(1, 21):
            s[i] = 1

    elif a[0] == "empty":
        s = [0] * m



'''
m = int(input())

act = []
s = []

for i in range(m):
    act.append(input().split())

for idx, a in enumerate(act):
    if a[0] == "add":
        s.append(a[1])

    if a[0] == "remove":
        s.remove(a[1])

    if a[0] == "check":
        try:
            if s.index(a[1]) != -1:
                print(1)
        except:
            print(0)

    if a[0] == "toggle":
        try:
            if s.index(a[1]) != -1:
                s.remove(a[1])
        except:
            s.append(a[1])

    if a[0] == "all":
        s = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]

    if a[0] == "empty":
        s = []

'''