#Вывести количество четный и нечетных елементов в рандомной последовательности.
import random
a = random.sample(range(30),4)
for i in range((30),4):
    #count even = 0
    #count odd = 0
    if a%2 == 0:
        print(a)
        a += 1
print(a)
