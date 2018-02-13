# _author: earl
# _data: 18/02/08
# -*- coding: utf-8 -*

# 购物车
goodsList = ['pingguo', 'pad', 'android', 'apple']
priceList = ['100', '2000', '1000', '3000']
selectGoodsList = []
priceTotal = 10000
selectGoodsPriceTotal = 0

print('---------- 货物价格如下 ------------')
for index, val in enumerate(goodsList):
    msg = '''
    number : %s
    name : %s
    price  : %s
    ''' % (str(index), val, priceList[index])
    print(msg)

while True:
    inputNber = input('请输入要购买的商品序号')
    if not inputNber:
        inputNber = '100'
    inputNber = int(inputNber)
    if not inputNber or inputNber > len(goodsList)-1:
        print('暂无此商品')
        continue
    else:
        if selectGoodsPriceTotal > priceTotal:
            print('你的钱已经花完，总得商品如下')
            selectGoodsList.pop(len(selectGoodsList)-1)
            for index, val in enumerate(selectGoodsList):
                good = '''
                name : %s
                price  : %s
                ''' % (goodsList[val], priceList[val])
                print(good)
            break
        else:
            selectGoodsList.append(inputNber)
            selectGoodsPriceTotal += int(priceList[inputNber])

            print('---------- 您购买的的商品如下 ------------')
            for index, val in enumerate(selectGoodsList):
                good = '''
                           name : %s
                           price  : %s
                           ''' % (goodsList[val], priceList[val])
                print(good)
