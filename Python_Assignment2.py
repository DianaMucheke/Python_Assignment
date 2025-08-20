my_list = []

list_1 = [10, 20, 30, 40]
my_list.extend(list_1)   # add elements, not the whole list
print(my_list)

my_list.insert(1, 15)
print(my_list)

my_list.extend([50, 60, 70])
my_list.pop()
print(my_list)

my_list.sort()
print(my_list)

print("Index of 30:", my_list.index(30))
