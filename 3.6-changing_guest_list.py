guest_list = ['bob', 'alice', 'john wick', 'rick', 'morty']

removed_name = guest_list.pop(4)

guest_list.append('bill')

print(f"{removed_name} can't make it")
print(f"{guest_list[0]} is invited")
print(f"{guest_list[1]} is invited")
print(f"{guest_list[2]} is invited")
print(f"{guest_list[3]} is invited")
print(f"{guest_list[4]} is invited")

print("there are more spots available")

guest_list.insert(0,'johnny')
guest_list.insert(3,'billy')
guest_list.append('steve')

print(f"{guest_list[0]} is invited")
print(f"{guest_list[1]} is invited")
print(f"{guest_list[2]} is invited")
print(f"{guest_list[3]} is invited")
print(f"{guest_list[4]} is invited")
print(f"{guest_list[5]} is invited")
print(f"{guest_list[6]} is invited")
print(f"{guest_list[7]} is invited")