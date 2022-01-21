total_count = 0
n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))
bridge = [0] * w

while True:
    bridge.pop(0)
    total_count += 1
    if len(trucks) > 0:
        if sum(bridge) + trucks[0] <= L:
            bridge.append(trucks.pop(0))
        else:
            bridge.append(0)
    if len(bridge) == 0:
        break
print(total_count)