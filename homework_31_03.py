# 1.Напишіть функцію, яка приймає два аргументи.
# Якщо обидва аргументи відносяться до числових типів, функція
# перемножує ці аргументи і повертає результат. Якшо обидва
# аргументи відносяться до типу стрінг функція обʼєднує їх
# в один і повертає. В будь - якому іншому випадку - функція повертає
# кортеж з двох агрументів.



# def test(a, b):
#     try:
#         print(a * b)
#         return a* b

#     except:
#         print(a + b)
#         return a + b

#     else:
#         print(a, b)


# test(3.4, 6.4)


def test(a, b):
    if type(a) and type(b) == int or type(a) and type(b) == float:
        print(a * b)
        return a * b
    elif isinstance(a, str) and isinstance(b, str):
        print(a + b)
        return a + b
    else:
        print(a, b)
        return a, b


test("Hi ","World") 




# 2. Візьміть код з заняття і доопрацюйте натупним
# чином: користувач має вгадати чизло за певну кількість спроб.користувач
# на початку програми визначає кількість спроб додайте підказки.якщо рвзнися
# між числами більше 10 - "холодно", від 10 до 5 - "тепло", 1 - 4 - "гаряче"

# AI -> numbers
#
# User get number from keyboard
#
# User == AI

# from random import randint

# def get_ai_number():
#     number = randint(1, 10)
#     print(f'AI: {number}')
#     return number


# def get_user_number():
#     while True:
#         try:
#             return  int(input('Enter the number: '))
#         except ValueError:
#             print('Number pls!')

# def check_numbers(ai_number, user_number):
#     result = ai_number == user_number
#     if result:
#         print(f'Result is, {result}')
#         return result
#     elif (ai_number - user_number) > 10:
#         print('Холодно!')
#     elif 5 < (ai_number - user_number) < 10:
#         print("Тепло!")
#     elif (ai_number - user_number) < 5:
#         print('Гаряче!')


# def game_guess_number():
#     print("Game begins!")
#     ai_number = get_ai_number()
#     user_tries = int(input("how many tries do you need?: "))
#     count = 1
#     while count <= user_tries:
#         user_number = get_user_number()
#         is_game_end = check_numbers(ai_number, user_number)
#         count += 1
#         if is_game_end:
#             break
#         print("Wrong, try again!")
# print("user wins!")

# game_guess_number()

