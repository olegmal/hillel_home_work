#1. Є list довільних чисел, наприклад [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44].
# Напишіть код, який видалить (не створить новий, а саме видалить!) з нього всі числа,
# які менше 21 і більше 74.

my_list = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]

i = 0
while i < len(my_list):
    if my_list[i] < 21 or my_list[i] > 74:
        del my_list[i]
    else:
        i +=1
print(my_list)





# 2.Є два довільних числа які відповідають за мінімальну і максимальну ціну.
# Є Dict з назвами магазинів і цінами: { "citos": 47.999, "BB_studio" 42.999, "mo-no": 49.999,
# "my-main-service": 37.245, "buy-now": 38.324, "x-store": 37.166, "the-partner": 38.988,
# "store-123": 37.720, "roze-tka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів,
# ціни яких потрапляють в діапазон між мінімальною і максимальною ціною.
#
# Наприклад:
# lower_limit = 35.9
# upper_limit = 37.339
# > match: "x-store", "main-service"

lower_limit = 35.9
upper_limit = 37.339

my_dict = { "citos": 47.999, "BB_studio": 42.999, "mo-no": 49.999,
            "my-main-service": 37.245, "buy-now": 38.324, "x-store": 37.166, "the-partner": 38.988,
            "store-123": 37.720, "rozetka": 38.003}

for key, value in my_dict.items():
    if value > lower_limit and value < upper_limit:
        print(key)


# # Інший варіант:

dict1 = ({key: v for key, v in my_dict.items() if v > lower_limit and v < upper_limit})

print("Назва магазів: ", list(dict1.keys()))