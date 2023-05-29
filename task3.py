things = {'bag': 3, 'sweater': 1, 'food': 3, 'music': 2, 'guitar': 4, 'boots': 5, 'wear': 4, 'pants': 2, 'alcohol': 5}
backpack = 10
my_list = []
for key, value in things.items():
    if backpack - value >= 0:
        backpack -= value
        my_list.append(key)
print(f'In my backpack are {my_list}')

