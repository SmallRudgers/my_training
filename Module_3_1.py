calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    rezult = (f'Длина слова: {len(string)}',string.upper(),string.lower())
    count_calls()
    return rezult

def  is_contains(string,list_to_search):
    rezult = False
    for i in list_to_search:
        if string.upper() == i.upper():
            rezult = True
            break
    count_calls()
    return rezult

print(string_info('Слово'))
print(string_info('Грусть'))
print(is_contains('Dad',['ded','moM','DaD']))
print(is_contains('Mom',['Dad','Sister']))
print('Количество вызовов функций:',calls)