#Посчитать количество 9 в списке.
l = [1,2,3,4,5,9,7,8,9]
count = 0
#[1,2,3,4,5,6,7,8,9]
for elem in l:
    if elem == 9 :
        print(elem)
        count = count + 1
print(count)
