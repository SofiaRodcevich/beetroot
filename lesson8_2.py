#Написать функцию поиска минимума в произвольном количестве элементов переданных в функцию
a = input().split(',')
#[5,10,7,13,9]

def minA(a):
    sortA = sorted(a)
    print(sortA[0])
    return sortA[0]

minA(a)
