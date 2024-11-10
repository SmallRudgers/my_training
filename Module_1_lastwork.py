grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_sort = list(students)
students_sort.sort()
grades_average_score = grades.copy()
result_students = {'1':'2'}
a = result_students.pop('1')

n=0

for i in grades:
    n+=1
    grades_average_score[n-1] = sum(grades[n-1])/len(grades[n-1])
    result_students.update({students_sort[n-1]:grades_average_score[n-1]})


print('Результат оценок:',result_students)



