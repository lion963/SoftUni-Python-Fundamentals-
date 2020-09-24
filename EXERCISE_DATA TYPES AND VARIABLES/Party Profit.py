party_size = int(input())
days = int(input())

companion = party_size
coins = 0

for day in range(1, days + 1):

    if day % 10 == 0:
        companion -= 2
    if day % 15 == 0:
        companion += 5
        coins-=2*companion

    coins += 50 - 2 * companion

    if day%3==0:
        coins-=3*companion
    if day%5==0:
        coins+=20*companion

coins_per=int(coins/companion)
print(f'{companion} companions received {coins_per} coins each.')