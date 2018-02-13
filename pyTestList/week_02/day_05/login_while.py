#_author: earl
#_data: 18/02/07
# -*- coding: utf-8 -*

_userName = 'earl'
_userPsd = '123'
counter = 0

while counter < 3:
    inputName = input('name: ')
    inputPsd = input('psd: ')
    if _userName == inputName and _userPsd == inputPsd:
        print('welcome %s login...' % inputName)
        break  # 跳出，中断 break 之后，就不会执行后边的else语句
    else:
        print('please try again only three now '+ str(counter+1) + ' number')
    counter += 1
    if counter == 3:
        keep_going_choice = input('还想玩吗？【y/n】')
        if keep_going_choice == 'y':
            counter = 0
else:#只要while循环没有被打断，正常执行完毕，就会执行else语句
    exit('try three not login')