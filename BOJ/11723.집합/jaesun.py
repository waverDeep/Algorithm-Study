import sys

m = int(sys.stdin.readline())

bit = 0
for _ in range(m):
    command = sys.stdin.readline().split()

    if command[0] == "all":
        bit = (1<<20)-1
    elif command[0] == "empty":
        bit = 0
    else:
        op = command[0]
        num = int(command[1]) - 1

        if op == "add":
            bit |= (1 << num)
        elif op == "remove":
            bit &= ~(1 << num)
        elif op == "check":
            if bit & (1 << num) == 0:
                print(0)
            else:
                print(1)
        elif op == "toggle":
            bit = bit ^ (1 << num)