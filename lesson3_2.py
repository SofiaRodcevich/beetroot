#Написать функцию, которая будет принимать пароль.
#Если его длина не менее 10 символов вывести: “Your password is strong.”
#в противном случае “Your password is not strong enough.”
password = str(input())
#a = password
def pas(password):
    A = [0,1,2,3,4,5,6,7,8,9]
    #return password

if len(password) > 10:
    print(str('Your password is strong.'))
else:
    print('Your password is not strong enough.')
