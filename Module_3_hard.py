def Element_Counter(element, Summa):

    if isinstance(element, (int, float)):
        Summa += element

    elif isinstance(element, str):
        Summa += len(element)

    elif isinstance(element, list):
        for i in element:
            Summa = Element_Counter(i, Summa)

    elif isinstance(element, tuple):
        for i in element:
            Summa = Element_Counter(i, Summa)

    elif isinstance(element, set):
        for i in element:
            Summa = Element_Counter(i, Summa)

    elif isinstance(element, dict):
        for key, value in element.items():
            Summa = Element_Counter(key, Summa)
            Summa = Element_Counter(value, Summa)
    return Summa

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

total_sum = Element_Counter(data_structure, 0)

print("Сумма всего:", total_sum)