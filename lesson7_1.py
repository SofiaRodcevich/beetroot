#Подсчитать количество каждого элемента в списке. Результат в виде словаря

L = input().split(',')
#[1,1,2,3,2]
d = {} #словарь
for elem in L:
    if elem in d:
        d[elem] = d[elem]+ 1
    else:
        d[elem] = 1
print(d)
