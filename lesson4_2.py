#Дан список чисел [1,2,3,4,5,6].
#Перемешать список с помощью функции random.shuffle
#и вывести случайное число с помощью random.choice
list = [1,2,3,4,5,6]
import random
random.shuffle(list)
print(list)
random.choice(list)
print(random.choice(list))
