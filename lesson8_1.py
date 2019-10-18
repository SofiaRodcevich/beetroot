#Написать функцию, которая будет принимать температуру по цельсию и возвращать ее перевод
#в температуру по фаренгейту по формуле: (temp - 32) * (5/9)
tempStr = input("enter temp:")
temp = int(tempStr)


def newTemp(temp):
    a = (temp - 32) * (5/9)
    print(a)
    return a

newTemp(temp)
