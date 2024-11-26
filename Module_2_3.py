my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n = 0
new_list = []

while my_list [n] >= 0:

    if my_list [n] > 0:
        new_list.append(my_list[n])

    n += 1

    if n == len(my_list):
        break

print(new_list)
