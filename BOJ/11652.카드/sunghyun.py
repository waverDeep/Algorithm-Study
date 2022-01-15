n = int(input())
cards = {}
for idx in range(n):
    card = int(input())
    if card in cards:
        cards[card] += 1
    else:
        cards[card] = 0
many = max(list(cards.values()))
pick = sorted([key for key, value in cards.items() if value == many])
print(pick[0])