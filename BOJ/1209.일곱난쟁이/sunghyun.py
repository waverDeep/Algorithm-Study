heights = []
for i in range(9):
    heights.append(int(input()))

out = []
for i in range(8):
    for j in range(i+1, 9):
        if sum(heights) - (heights[i] + heights[j]) == 100:
            out.append(heights[i])
            out.append(heights[j])

heights.remove(out[0])
heights.remove(out[1])
heights.sort()
for height in heights:
    print(height)