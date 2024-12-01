def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if number == 0:
        return 1
    else:
        return first * get_multiplied_digits(number % (10**(len(str_number)-1)))


rezult_1 = get_multiplied_digits(120302)
print(rezult_1)

rezult_2 = get_multiplied_digits(2980002301230)
print(rezult_2)