#1
immutable_var = (3,"Кортеж", True, 2.4, [1,2,3,4])
print("Immutable tuple:",immutable_var)

#2
#В кортеже можно изменить только списки. Остальные переменные неизменны.
#immutable_var [1] = 3 -> в этом случае будет ошибка
#print(immutable_var)

#3
mutable_list = ([1, 2, 3, 4.5, 'Победа'], [2,1], 'tuples')
mutable_list[0][4] = 9
print("Mutable list:",mutable_list)
