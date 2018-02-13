# -*- coding:UTF-8 -*-
# 使用给定的宽度打印格式化后的价格
_width = input('Please enter width: ')
_width = int(_width)
price_width = 10
item_width = _width - price_width
header_format = '%-*s%*s'
format = '%-*s%*.2f'
print('='*_width)
print (header_format % (item_width,'Item',item_width,'Price'))
print ('-' * _width)
print (format % (item_width,'Apples1',price_width,0.41))
print (format % (item_width,'Apples2',price_width,0.42))
print (format % (item_width,'Apples3',price_width,0.43))
print (format % (item_width,'Apples4',price_width,0.44))
print (format % (item_width,'Apples5',price_width,0.45))
print (format % (item_width,'Apples6',price_width,0.46))

print ('=' * _width)
print ('item_width=%s'% item_width)