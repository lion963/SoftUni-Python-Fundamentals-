class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            species_names = self.mammals
        elif species == 'fish':
            species_names = self.fishes
        elif species == 'bird':
            species_names = self.birds
        names = ', '.join(species_names)
        if species == 'mammal':
            return f'Mammals in {zoo.name}: {names}'
        elif species == 'fish':
            return f'Fishes in {zoo.name}: {names}'
        elif species == 'bird':
            return f'Birds in {zoo.name}: {names}'

    def get_total(self):
        return f'Total animals: {self.__animals}'


zoo_name = input()
zoo = Zoo(zoo_name)

n = int(input())
for _ in range(n):
    species, name = input().split(' ')
    zoo.add_animal(species, name)

species = input()

print(zoo.get_info(species))
print(zoo.get_total())
