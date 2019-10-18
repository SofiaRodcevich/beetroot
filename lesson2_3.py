# 3) Написать функцию, которая будет принимать номер телефона
#  и выводить его в формате +38 (099) 123 - 12 - 12
code1 = "+38 "
code2 = "(099)"
code3 = " 123 "
code4 = "- 12 "
code5 = "- 12 "
def ph_number(code1, code2,code3, code4, code5):
 return(code1 + code2 + code3 + code4 +code5)

function_res = ph_number(code1, code2, code3, code4, code5)
print(function_res)
