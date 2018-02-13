#_author: earl
#_data: 18/02/07
# -*- coding: utf-8 -*
exit_flag = False
for i in range(10):
    if i<5:
        continue
    print(i)
    for j in range(10):
        print("layer2",j)
        if j == 6:
            exit_flag = True #如果子循环跳出，父循环直接退出
            break #只跳出当前循环
    if exit_flag:
        break
