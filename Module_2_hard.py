import random

Random_num = random.randint(3,20)
exception = []
Win_num = []
n = 0

for i in range(1,20):
    if i <= Random_num:
        for k in range(1,20):

            if k >= Random_num:
                break
            elif i != k and i != Random_num and k != Random_num and Random_num % (i + k) == 0:
                for j in exception:
                    if j == k:
                        n+=1
                if n < 1:
                    Win_num.append([i, k])
                else:
                    n = 0
    else:
        break
    exception.append(i)

print(f'Сгенерерованное число: {Random_num}\nРешение задачи:', *Win_num)
