#_author: earl
#_data: 18/02/07
# -*- coding: utf-8 -*
#包含 列表的增、删、改、查、排序

#（增）添加 1、append 2、insert 3、extend
#1、append
aList = ['zhangshan','lisi','xiaohu','sanpang','wangwu']
aList.append('zhanglong') # 在列表末尾添加数据
print(aList)              #['zhangshan', 'lisi', 'xiaohu', 'sanpang', 'wangwu', 'zhanglong']
#2、insert
aList.insert(1,'huangtao')# 指定列表位置插入，第一个参数是要插入的索引，第二个参数为要插入的数据
print(aList)              # ['zhangshan', 'huangtao', 'lisi', 'xiaohu', 'sanpang', 'wangwu', 'zhanglong']
#3、extend扩展，添加另一个集合
list_01 = [1,2,3]
list_02 = [4,5,6]
list_01.extend(list_02)   #扩展list_01
print(list_01)            #[1, 2, 3, 4, 5, 6]

#（删）删除 1、remove 2、pop 3、del
#1、remove
aList = ['zhangshan','lisi','xiaohu','sanpang','wangwu']
aList.remove(aList[0]) # 要删除的内容,只能是一个元素不能是列表,根据内容删除，无返回
print(aList)           # ['lisi', 'xiaohu', 'sanpang', 'wangwu']
#2、pop
aList = ['zhangshan','lisi','xiaohu','sanpang','wangwu']
print(aList.pop(0) )   # 删除索引为0的值，根据索引删除，返回删除的值 zhangshan
print(aList)           # ['lisi', 'xiaohu', 'sanpang', 'wangwu']
#3、del
aList = ['zhangshan','lisi','xiaohu','sanpang','wangwu']
del aList[0]           # 删除指定内容，可以是列表数据，无返回值
print(aList)           # ['lisi', 'xiaohu', 'sanpang', 'wangwu']
aList = ['zhangshan','lisi','xiaohu','sanpang','wangwu']
del aList[0:4]         # 删除列表数据
print(aList)           # ['wangwu']

#（改）修改 1、x[1] = 'date' 2、x[:] = [y,z]
#1、x[1] = 'date'
aList = ['zhangshan','lisi','xiaohu','sanpang','wangwu']
aList[1] = 'dahai'                  # 单个数值的修改
print(aList)                        # ['zhangshan', 'dahai', 'xiaohu', 'sanpang', 'wangwu']
#2、x[:] = [y,z]
aList[1:3] = ['dahai1','xiaohu1']   # 对一组数据进行修改
print(aList)                        # ['zhangshan', 'dahai1', 'xiaohu1', 'sanpang', 'wangwu']

#（查）切片 ﻿查找数据 1、x[:] 2、count查某个元素的出现次数 3、index 4、in（字符串使用）
#1、x[:]
aList = ['zhangshan','lisi','xiaohu','sanpang','wangwu']
print(aList[1:])    # 取值到最后 ['lisi', 'xiaohu', 'sanpang', 'wangwu']
print(aList[1:-1])  # 取到倒数第二个数值 ['lisi', 'xiaohu', 'sanpang']
print(aList[1:-1:1])# 取到倒数第二个数值，一个一个取 ['lisi', 'xiaohu', 'sanpang']
print(aList[1::2])  # 从左到右隔一个取一个 ['lisi', 'sanpang']
print(aList[3::-2]) # 从右到左隔一个取一个数值，步长中-2的负数代表方向，正方向是从左到右取值 [ 'sanpang', 'lisi']
#2、count
bList = ['to','to','be','bt','bu']
print(bList.count('to'))   # 返回元素'to'在bList列表中的个数
#3、index
aList = ['zhangshan','lisi','xiaohu','sanpang','wangwu']
print(aList.index('lisi')) # 取出‘list’在列表的索引值
#4、in（字符串使用）
print('z' in 'zhang') #字符串使用 True

#（排序） 1、reverse倒序 2、sort排序
#1、reverse倒序
aList = ['zhangshan','lisi','xiaohu','sanpang','wangwu']
aList.reverse()            # 倒序排列，无返回值
print(aList)               # ['wangwu', 'sanpang', 'xiaohu', 'lisi', 'zhangshan']
#2、sort排序
aList = [2,3,4,1,5,7]
aList.sort()               # 按照ASCII正序排序，无返回值
print(aList)               # [1, 2, 3, 4, 5, 7]
aList = [2,3,4,1,5,7]
aList.sort(reverse = True) #按照ASCII倒序排序，无返回值
print(aList)               #[7, 5, 4, 3, 2, 1]
