# 1.створити АРІ на базі гугл таблиці, містить поля "назва товару", "опис товару", "ціна"
# (інтова чи флоат), "залишок"(інтовий чи флоат), "містить глютен"(булеве
# тру чи фолс(виставляєте прапорцем).заповнити мінімум 10 позицій.дані мають
# бути отримати по зовнішньому ключу "goods"(not "data") за допомогою requests завантажити
#2. створені дані.порахувати вартість всіх товарів та товарів без глютена.



import requests
from pprint import pprint

response = requests.get("https://script.googleusercontent.com/macros/echo?user_content_key=bCswtSZ2xEO_387FqoqYEYc6u3UJngC2oWza7DmTwkHmyLbawNl8T5uLIl3rRBVIJi8CXg2f6ccQhpWviGL212q-EJxbBvn_m5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnBaELiLaT1O-y7WdxSZAznba4uwc1FIEHpAALm4POcNBC4jo7PwEh-noBMaw4s32FMGGdnnhNvgc4qf-5yVaPaHO1STXF_M8Vw&lib=MMLdW_cURExqyjhNKIXjNjPnf2Uzy0fRy")
goods = response.json()
data = goods.get('data', [])
# pprint(goods)

cost_of_goods = 0
nongluten_goods = 0

for good in data:
    price = good.get('price', 0)
    stock = good.get('stock balance', 0)
    goods_cost = price * stock
    cost_of_goods += goods_cost
    print(f'Загальна вартість залишків товару: {cost_of_goods}')
    if good.get("contains gluten", 0) == False:
        nongluten_goods += goods_cost
        print(f"Товар без глютену:{nongluten_goods}")






