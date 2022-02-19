N = int(input())
score = [0] * 300
dp_table = [0] * 300
for i in range(N):
    score[i] = int(input())

dp_table[0] = score[0]
dp_table[1] = max(score[0] + score[1], score[1])
dp_table[2] = max(score[0] + score[2], score[1] + score[2])
for i in range(3, N):
    dp_table[i] = max(dp_table[i - 2] + score[i], dp_table[i - 3] + score[i - 1] + score[i])

print(dp_table[N - 1])