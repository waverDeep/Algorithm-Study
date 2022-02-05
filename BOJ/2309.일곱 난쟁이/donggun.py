originalTall = []

for i in range(9):
    originalTall.append(int(input()))

tall = originalTall.copy()

check = False

for i in range(9):
    for j in range(9):

        if i > j:
            tall.remove(tall[i])
            tall.remove(tall[j])

        else:
            tall.remove(tall[i])
            tall.remove(tall[j - 1])

        if sum(tall) == 100:

            for k in sorted(tall):
                print(k)
            check = True

        if check:
            break
        tall = originalTall.copy()

    if check:
        break