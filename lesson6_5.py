#Посчитать факториал для введенного пользователем числа
a = int(input())
factorial = 1
for i in range(2, a+1):
    factorial *= i

print(factorial)
