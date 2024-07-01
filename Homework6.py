my_dict = {'Ivan': 1985, 'Sergey': 1989, 'Andrey': 1991}
print(my_dict)
print(my_dict.get('Ivan'))
print(my_dict.get('Anton'))
my_dict.update({'Sasha': 1990, 'Max': 1982})
name = my_dict.pop('Andrey')
print(name)
print(my_dict)

my_set = {1, 2, 3, 4, 5, "Ivan", "Andrey", 3, 1, 5, 'Ivan'}
print(my_set)
my_set.update({7, 'Max'})
my_set.discard(2)
print(my_set)