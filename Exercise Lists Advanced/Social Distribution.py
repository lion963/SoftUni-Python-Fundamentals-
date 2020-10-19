wealth_list = list(map(int, input().split(', ')))
minimum_wealth = int(input())

if sum(wealth_list)<len(wealth_list)*minimum_wealth:
    print(f'No equal distribution possible')
else:
    for i in range(len(wealth_list)):
        if wealth_list[i] < minimum_wealth:
            index = wealth_list.index(max(wealth_list))
            wealth_list[index] -= (minimum_wealth - wealth_list[i])
            wealth_list[i] += minimum_wealth - wealth_list[i]
    print(wealth_list)