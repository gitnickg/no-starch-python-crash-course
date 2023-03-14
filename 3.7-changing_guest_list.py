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

removed_name_1 = guest_list.pop(0)
removed_name_2 = guest_list.pop(1)
removed_name_3 = guest_list.pop(2)
removed_name_4 = guest_list.pop(3)
#removed_name_5 = guest_list.pop(5)

print("there are only two tables now")
print(f'{removed_name_1} is off the list')
print(f'{removed_name_2} is off the list')
print(f'{removed_name_3} is off the list')
print(f'{removed_name_4} is off the list')
#print(f'{removed_name_5} is off the list')


print(f"{guest_list[0]} is invited")
print(f"{guest_list[1]} is invited")

del guest_list[0]
del guest_list[1]

print(guest_list)
