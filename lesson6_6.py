#С помощью random сгенерировать 2 целых числа и спросить у пользователя ответ суммы этих чисел.
#Если пользователь посчитал верно то засчитать ему одно очко. Повторять пока пользователь не введет ‘q’.
import random

point = 0
while True:
    x = random.randint(0,10)
    y = random.randint(0,10)
    print('points:' + str(point))
    answer = input(str(x) + '+' +str(y) +'=?(type q to quit):')
    if answer == 'q':
        break
    elif int(answer) != x+y:
        print('No point for you!')
        continue
    print('Good job')
    point += 1
