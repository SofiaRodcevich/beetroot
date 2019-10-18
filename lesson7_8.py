#Генерируется квадратная матрица (с помощью списковых включений).
#Найти сумма элементов ее главной и побочной диагоналей.
a = [[1,2,3],[2,3,4],[3,4,5]]
n=3
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = '')
    print()

sumMain = 0
sumSecondary = 0
for i in range(n):
    sumMain += a[i][i]
    sumSecondary += a[i][n-i-1]

print(sumMain)
print(sumSecondary)
