from hash import HashTable


def menu_insert():
    print('Please, input identifier that you want to insert')
    key = input()
    try:
        hash_table.insert(key)
    except KeyError as e:
        print(e)


def menu_find():
    print('Please, input identifier that you want to find')
    key = input()
    cmp_count = [0]
    found = hash_table.find(key, cmp_count)
    if found is None:
        print('This identifier not found')
    else:
        while found is not None:
            print(found.identifier)
            print('^')
            print('|')
            found = found.parent
        print('HashTable[' + str(HashTable.hash_func(key)) + ']')
        print('Count of comparisons is ' + str(cmp_count[0]))


def print_menu():
    print("1. Insert")
    print("2. Find")
    print("3. Average number of collisions")
    print("4. Exit")


hash_table = HashTable()
file = open("input.txt", "r")
i = 1
for line in file:
    if line[len(line) - 1] == '\n':
        hash_table.insert(line[0:len(line) - 1])
    else:
        hash_table.insert(line)
menu_item = '0'
while menu_item != '4':
    print_menu()
    menu_item = input()
    if menu_item == '1':
        menu_insert()
    elif menu_item == '2':
        menu_find()
    elif menu_item == '3':
        print(hash_table.get_avg_collisions())
    elif menu_item == '4':
        print('Press enter, to exit')
        input()
    else:
        print('No such menu item')
