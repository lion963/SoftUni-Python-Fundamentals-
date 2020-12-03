class PlacesOfStops:

    def __init__(self, places):
        self.places = places

    def add_stop(self, index, string):
        if 0 <= index < len(self.places):
            self.places = self.places[:index] + string + self.places[index:]

    def remove_stop(self, start_in, stop_in):
        if 0 <= stop_in < len(self.places) and 0 <= stop_in < len(self.places) and start_in <= stop_in:
            self.places = self.places[:start_in] + self.places[stop_in + 1:]

    def switch(self, old_str, new_str):
        if old_str in self.places:
            self.places = self.places.replace(old_str, new_str)

    def __repr__(self):
        return f'{self.places}'


stops_str = input()
stops_obj = PlacesOfStops(stops_str)

line = input()
while not line == 'Travel':
    command_list = line.split(':')

    if command_list[0] == 'Add Stop':
        stops_obj.add_stop(int(command_list[1]), command_list[2])
        print(stops_obj)

    elif command_list[0] == 'Remove Stop':
        stops_obj.remove_stop(int(command_list[1]), int(command_list[2]))
        print(stops_obj)

    elif command_list[0] == 'Switch':
        stops_obj.switch(command_list[1], command_list[2])
        print(stops_obj)

    line = input()

print(f'Ready for world tour! Planned stops: {stops_obj}')

# stops_str = input()
#
# line = input()
# while not line == 'Travel':
#     command_list = line.split(':')
#
#     if command_list[0] == 'Add Stop':
#         if 0 <= int(command_list[1]) <= len(stops_str):
#             stops_str = stops_str[:int(command_list[1])] + command_list[2] + stops_str[int(command_list[1]):]
#             print(stops_str)
#
#     elif command_list[0] == 'Remove Stop':
#         if 0 <= int(command_list[1]) < len(stops_str) and 0 <= int(command_list[2]) < len(stops_str) and int(
#                 command_list[1]) <= int(command_list[2]):
#             stops_str = stops_str[:int(command_list[1])] + stops_str[int(command_list[2]) + 1:]
#             print(stops_str)
#
#     elif command_list[0] == 'Switch':
#         if command_list[1] in stops_str:
#             stops_str = stops_str.replace(command_list[1], command_list[2])
#             print(stops_str)
#
#     line = input()
#
# print(f'Ready for world tour! Planned stops: {stops_str}')
