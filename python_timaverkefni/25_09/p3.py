def make_list():
    initial_list = []
    item = input("Enter value to be added to list: ")
    initial_list.append(item)
    while item != 'exit' and item != 'Exit' and item != 'EXIT':
        item = input("Enter value to be added to list: ")
        initial_list.append(item)
    initial_list.pop()
    return initial_list

l = make_list()
new_list = l * 3

for items in new_list:
    print(items)