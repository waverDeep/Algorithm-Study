def n_gram(data):
    add_line = []
    for i in range(len(data) - 1):
        add_line.append(int(data[i]) - int(data[i + 1]))
    return add_line


num = int(input())

if num < 100:
    print(num)
else:
    count = 0
    for i in range(100, num + 1):
        data = list(str(i))
        output = n_gram(data[::-1])

        if output[0] == output[1] and i != 1000:
            count += 1

    print(count + 99)
