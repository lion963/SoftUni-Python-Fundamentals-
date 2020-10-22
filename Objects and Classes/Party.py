class Party:
    def __init__(self):
        self.people = []

    def add_people(self, person):
        self.people.append(person)

    def party_info(self):
        print(f"Going: {', '.join([person.name for person in self.people])}")

    def total(self):
        print(f'Total: {len(self.people)}')


class Person:
    def __init__(self, name):
        self.name = name


party = Party()

while True:
    command = input()
    if command == 'End':
        break
    name = command
    person = Person(name)
    party.add_people(person)

party.party_info()
party.total()
