#_author: earl
#_data: 18/02/06
# -*- coding: utf-8 -*
name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")

if salary.isdigit():#长的像数字，步入'200'
    salary = int(salary)
else:
    exit('must input digit')#退出程序

msg = '''
---------- info of %s ------------
Name : %s
Age  : %d
Job  : %s
Salary : %f
You will be retired in %s years
''' % (name,age,job,salary,65-age)

print(msg)