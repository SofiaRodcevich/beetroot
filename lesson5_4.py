#Написать функцию, которая принимает 2 списка и возвращает True если первые или последние элементы списка равны
ls1 = input()
ls2 = input()

def result(ls1,ls2):
    return ls1 + ls2

result1 = result(ls1,ls2)
if ls1[0] == ls2[0] or ls1[-1] == ls2[-1]:
        print(True)
else:
        print(False)
