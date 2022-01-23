A = input()
T = input()
left_idx = 0
right_idx = len(T) - 1
left_stack = []
right_stack = []

while left_idx <= right_idx:
    while left_idx <= right_idx:
        left_stack.append(T[left_idx])
        left_idx += 1
        if len(left_stack) >= len(A) and ''.join(left_stack[-len(A):]) == A:
            del left_stack[-len(A):]
            break

    while left_idx <= right_idx:
        right_stack.append(T[right_idx])
        right_idx -= 1
        if len(right_stack) >= len(A) and ''.join(right_stack[-len(A):]) == A[::-1]:
            del right_stack[-len(A):]
            break
line = left_stack + right_stack[::-1]
ti = 0
while ti >= 0:
    ti = ''.join(line).find(A)
    if ti != -1:
        del line[ti:ti + len(A)]
print(''.join(line))