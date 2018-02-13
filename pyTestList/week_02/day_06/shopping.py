#_author: earl
#_data: 18/02/08
# -*- coding: utf-8 -*

#购物车
goodsList = ['pengguo','pad','android','apple']
priceList = ['100','2000','1000','3000']
selectGoodsList = []
priceTotal = 10000
selectGoodsPriceTotal = 0

for index,val  in enumerate(goodsList):
    msg = '''
    '---------- 货物 (%s) 价格 ------------'
    name : %s
    price  : %s
    ''' % (str(index), val, priceList[index])
    print(msg)

while True:
    inputNber = int(input('请输入要购买的商品序号'))
    if inputNber > len(goodsList):
        print('暂无此商品')
        continue
    else:
        if selectGoodsPriceTotal > priceTotal:
            print('你的余额不足')
            selectGoodsPriceTotal+=priceList[inputNber]



