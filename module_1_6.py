#1 работа с словарем
my_dict = {'Key1': 23,'Key2': 47 }

print (f"Словарь: {my_dict}")
print (f"1) Значение ключа 'Key1': {my_dict['Key1']}")
print (f"2) Значение отсутствующего ключа 'Key3': {my_dict.get('Key3')}\n")

my_dict.update ({'Key3': 12,'Key4': 543})
print (f"Обновленный словарь: {my_dict}")

taken_key = my_dict.pop('Key2')
print (f"4)Значение изъятого ключа 'Key2': {taken_key}")
print (f"5)Словарь после изъятия ключа: {my_dict}\n")

#2 работа с множеством
my_set = {2, 2 ,14 ,6, 23, 6, 'Яблоко', 'Яблоко'}
print("Множество:", my_set)
my_set.update([213213, 4435])
my_set.discard(2)
print("Обновленное множество:", my_set)
