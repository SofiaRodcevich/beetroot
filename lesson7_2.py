#Вывести количество четный и нечетных елементов в рандомной последовательности.
#Результат в виде словаря
import random
d = {'even':0, 'odd':0}
a = random.sample(range(0,100),10)


print(a)
for elem in a:
    if elem % 2 == 0:
        d['even'] = d['even'] + 1
    else:
        d['odd'] = d['odd'] + 1

print(d)
