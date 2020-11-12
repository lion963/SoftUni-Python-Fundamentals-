company_dict = {}

line = input()
while not line == 'End':
    company, id = line.split(' -> ')

    if company not in company_dict:
        company_dict[company] = []
    if id not in company_dict[company]:
        company_dict[company].append(id)

    line = input()

company_dict = dict(sorted(company_dict.items()))
for key, value in company_dict.items():
    print(key)
    for el in value:
        print(f'-- {el}')
