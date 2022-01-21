while True:
    input_data = input()
    if input_data == '.':
        break
    input_data = input_data.replace(' ', "")
    stack = []
    for character in input_data:
        if character == '(' or character == '[':
            stack.append(character)
        elif character == ')':
            if len(stack) != 0:
                last = stack.pop()
                if last != '(':
                    print("no")
                    stack = None
                    break
            else:
                print("no")
                stack = None
                break
        elif character == ']':
            if len(stack) != 0:
                last = stack.pop()
                if last != '[':
                    print("no")
                    stack = None
                    break
            else:
                print("no")
                stack = None
                break
    if stack is not None:
        if len(stack) == 0:
            print("yes")
        else:
            print("no")
