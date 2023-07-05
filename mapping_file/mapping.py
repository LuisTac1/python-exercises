"""
Data mapping
"""

from data import products, people, list1
from functools import reduce


new_list = map(lambda x: x * 2, list1)

new_list =[x * 2 for x in list1]
print(list1)
print(list(new_list))


def raise_prices(p):
    p['price'] = round(p['price'] * 1.05, 2)
    return p

new_products = map(raise_prices, products)

for p in products:
    print(p)

for p in new_products:
    print(p)

names = map(lambda p: p['name'], people)

for i in names:
    print(i)


"""filter"""

# new_list = filter(lambda p: p['price'] > 50, products)

# def filt(pessoa):
#     if pessoa['age'] >= 18:
#         return True

# new_list = filter(filt, people)

# for product in new_list:
#     print(product)


"""Reduce"""

# accumul =0

# for item in list1:
#     accumul += item

# print(accumul)


# sum_list1 = reduce(lambda ac, i: i + ac, list1, 0)

# sum_price = reduce(lambda ac, p: p['price'] + ac, products, 0)

# print(sum_price)
