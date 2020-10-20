needed_money=float(input())
months=int(input())

collected_money=0

for i in range(1,months+1):

    if not i%2==0 and not i==1:
        collected_money-=collected_money*0.16

    if i%4==0:
        collected_money+=collected_money*0.25

    collected_money+=needed_money*0.25

if collected_money>=needed_money:
    print(f'Bravo! You can go to Disneyland and you will have {(collected_money-needed_money):.2f}lv. for souvenirs.')
else:
    print(f'Sorry. You need {(needed_money-collected_money):.2f}lv. more.')