my_dict = {'Nikolai': 1998,'Sebastian': 1988,'Ivan': 1944}
print(my_dict)
print(my_dict['Nikolai'])
print(my_dict.get('Viktor','Такого нет')) #- Решил заменить Nоne на слово
my_dict.update({'Malvina': 2000,'Sveta': 1999})
a = my_dict.pop('Sebastian')
print(a)
print(my_dict)

my_set = {1,2,4,5,3.2,'Nikola',4,3.2,1,'Nikola',True,(1,2,3)}
print(my_set)
my_set.add('яблоко')
my_set.add(18)
my_set.remove('Nikola')
print(my_set)
