import re

data = input()
data_dict = {}
days=0
calories_per_day = 2000

pattern = r'(?P<sep>\#|\|)(?P<product>[A-Za-z ]+)(?P=sep)(?P<date>\d{2}/\d{2}/\d{2})(?P=sep)(?P<calories>\d+)(?P=sep)'

result = re.finditer(pattern, data)
if result:
    for el in result:
        products = el.groupdict()
        if 'product' not in data_dict:
            data_dict['product'] = [products['product']]
        else:
            data_dict['product'] += [products['product']]
        if 'date' not in data_dict:
            data_dict['date'] = [products['date']]
        else:
            data_dict['date'] += [products['date']]
        if 'calories' not in data_dict:
            data_dict['calories'] = [int(products['calories'])]
        else:
            data_dict['calories'] += [int(products['calories'])]
if data_dict:
    total_calories = sum(data_dict['calories'])
    days += total_calories // calories_per_day
    print(f'You have food to last you for: {days} days!')
    for i in range(len(data_dict['product'])):
        print(f"Item: {data_dict['product'][i]}, Best before: {data_dict['date'][i]}, Nutrition: {data_dict['calories'][i]}")
else:
    print(f'You have food to last you for: {days} days!')
