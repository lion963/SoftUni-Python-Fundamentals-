import re

places_str = input()
destinations = []
points = 0

pattern = r'(?P<sep>\=|\/)(?P<location>[A-Z][A-Za-z]{2,})(?P=sep)'
if re.finditer(pattern, places_str):
    result = re.finditer(pattern, places_str)
    for el in result:
        location = el.groupdict()['location']
        destinations.append(location)

if destinations:
    for el in destinations:
        points += len(el)

print(f"Destinations: {', '.join(destinations)}")
print(f'Travel Points: {points}')

# r'(?<=(?P<sep>\=|\/))(?P<location>[A-Z][A-Za-z]{2,})(?=(?P=sep))'
