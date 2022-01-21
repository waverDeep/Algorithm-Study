n = int(input())
for idx in range(n):
    line = input()
    stack = []
    for character in line:
        if character == '(':
            stack.append(character)
        elif character == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                print("NO")
                stack = None
                break
    if stack is not None:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")