def print_params(a=1, b='строка', c=True):
    print(a,b,c,'\n')

list_ = ['Замена', 45]

print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*list_)

values_list = ['Listiki', 1 , False]
values_dict = {'a':'key', 'b':2.23, 'c':False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['?',55]
print_params(*values_list_2, 42)