# -*- coding: utf-8 -*
print('字典dict')
d = {'michael' : 96 , 'bob' : 75 , 'tracy' : 85} # 字典初始化赋值
print(d['michael']) # 字典取值
d['michael'] = 100 # 字典赋值
print(d['michael'])
print(d.get('name')) # 查看key是否存在,不存在就为None
print(d.get('michael')) # 查看key是否存在,存在就把值返回
d.pop('michael') # 删除指定key
print(d)
print('+++++++++++++++++++++++++')
print('set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。')
s = set([1,2,3]) # 存入列表
print(s)

s1 = set((1,2,3)) # 存入元组
print(s1)

s2 = [1,2,3]
s2_1 = set(s2)
print(s2_1)

