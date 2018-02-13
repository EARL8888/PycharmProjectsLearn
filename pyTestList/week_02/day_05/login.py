#_author: earl
#_data: 18/02/06
# -*- coding: utf-8 -*

# for i in range(1,101,2): #2 步长
#     print("loop:",i) #1357... 隔两步取一个值

_userName = 'earl'
_userPsd = '123'

# passed_authentication = False #设置标记卫
#
# for i in range(3):#range(3) = [0, 1, 2]
#     inputName = input('name: ')
#     inputPsd = input('psd: ')
#     if _userName == inputName and _userPsd == inputPsd:
#         print('welcome %s login...' % inputName)
#         passed_authentication = True # 真，成立
#         break #跳出，中断
#     else:
#         print('please try again')
#
# if not passed_authentication: #只在True的情况下，条件成立
#     exit('try three not login')

#---------------- 以下同上操作 -----------------------------------

for i in range(3):
    inputName = input('name: ')
    inputPsd = input('psd: ')
    if _userName == inputName and _userPsd == inputPsd:
        print('welcome %s login...' % inputName)
        break #跳出，中断 break 之后，就不会执行后边的else语句
    else:
        print('please try again')
else:#只要for循环没有被打断，正常执行完毕，就会执行else语句
    exit('try three not login')