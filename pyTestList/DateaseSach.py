# -*- coding:UTF-8 -*-
database = [
    ['zhangsan', '123'],
    ['lisi', '321'],
    ['zhaosi', '132']
]
username = input('user_name:')
pin = input('pin:')
if [username, pin] in database:
    print('登录成功')
else:
    print('登录失败')
