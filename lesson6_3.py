#Пользователь должен ввести последовательность чисел через пробел.
#Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось
#в последовательности или NO, если не встречалось.
L = input().split()
#print(L.split())
#L = map(int, L)
S = set()
for element in L:
    if element in S:
        print('Yes')
    else:
        print('No')
        S.add(element)
