#Написать функцию, которая принимает 3 списка и возвращает их общую сумму элементов

# a = input()
# b = input()
# c = input()
ls1 = sum(map(int, list(input().split())))
ls2 = sum(map(int, list(input().split())))
ls3 = sum(map(int, list(input().split())))
L = ls1 + ls2 + ls3
print(L)



# def summa(ls1,ls2,ls3):
#     return ls1 + ls2 + ls3
# summa = ls1[:], ls2[:], ls3[:]
# print (summa)
