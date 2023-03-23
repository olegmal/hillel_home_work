#1. Напишіть цикл, який буде вимагати від користувача ввести слово,
# в якому є буква "о" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися,
# якщо користувач ввів слово без букви "о".



while True:
    my_word = input("Pls, enter word, containing 'o': ")
    if 'o' in my_word:
        print(my_word)
        break

    print("Word does not contain 'o'")


#2. Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг,
# які присутні в lst1. Зауважте, що lst1 не є статичним і може формуватися динамічно від запуску до запуску.

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
my_list = []
for item in lst1:
    if type(item) == str:
        my_list.append(item)
print(my_list)

# 3.Є стрінг з певним текстом (можна скористатися input або константою).
# Напишіть код, який визначить кількість слів в цьому тексті, які закінчуються на "о"
# (враховуються як великі так і маленькі).

my_string = "Alice said Hello and went to her friend."
print(len([words for words in my_string.split(' ') if words[-1] == 'o']))