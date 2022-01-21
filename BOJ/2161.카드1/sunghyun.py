import queue
q = queue.Queue()
trash = []
n = int(input())
for data in range(1, n+1):
    q.put(data)
while q.qsize() != 1:
    # step-1
    trash.append(q.get())
    # step-2
    q.put(q.get())
trash.append(q.get())

for t in trash:
    print(t, end=' ')