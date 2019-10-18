#Создать файл nums.txt с рандомными цифрами и нужно среди них найти самую большую цифру
#и написать его уже в новый max_num.txt файл
#f = open('nums.txt' , 'r')
#read_data = f.read()
#f.close()
#print(read_data)
#print(max(read_data))


# import random
# with open('nums.txt', 'w') as op_f:
#     rnd_s = random.sample(range(1,50),10)
#     rnd_s_str = ','.join(map(str, rnd_s))
#     op_f.write(rnd_s_str)
# with open('nums.txt' , 'r') as op_f:
#     r_obj = op_f.read()
#     r_obj1 = r_obj.split(',')
#     print(r_obj1)

#
def initPoints():
    points = []
    f = open('C:\\Users\\38095\\Desktop\\практика\\labs\\python\\lab1\\PYTHON.py\\nums.txt')
    points = max(f.read().split(','))
    f.close()
    print(points)


initPoints()
