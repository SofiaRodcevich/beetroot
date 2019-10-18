#Написать функцию для подсчета периметра фигуры в зависимости от того какую фигуру укажет пользователь
figure = input("Enter square, triangle or rectangle" + "\n")

def summa_square():
  res1 = input("Please, enter square side" + "\n")
  res1 = int(res1)
  res1 = res1*4
  return(res1)

def summa_triangle():
  a = input("Please, enter triangle 1 side" + "\n")
  b = input("Please, enter triangle 2 side" + "\n")
  c = input("Please, enter triangle 3 side" + "\n")
  res1 = int(a) + int(b) + int(c)
  return(res1)


def summa_rectangle():
  a = input("Please, enter rectangle 1 side" + "\n")
  b = input("Please, enter rectangle 2 side" + "\n")
  res1 = 2*(int(a) + int(b))
  return(res1)

perimetr = 0
if figure == "square":
  perimetr = summa_square()

if figure == "triangle":
  perimetr = summa_triangle()

if figure == "rectangle":
  perimetr = summa_rectangle()

print(perimetr)
