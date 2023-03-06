guest_list = ['bob', 'alice', 'john wick', 'rick', 'morty']

removed_name = guest_list.pop(4)

guest_list.append('bill')

print(f"{removed_name} can't make it")
print(f"{guest_list[0]} is invited")
print(f"{guest_list[1]} is invited")
print(f"{guest_list[2]} is invited")
print(f"{guest_list[3]} is invited")
print(f"{guest_list[4]} is invited")