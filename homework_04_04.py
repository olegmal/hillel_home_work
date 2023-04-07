# 1.Напишіть функцію, яка визначає сезон за датою.
# Функція отримує стрінг у форматі "[день].[місяць]" (наприклад "12.01", "30.08", "1.11" і тд)
# і повинна повернути стрінг з відповідним сезоном,
# до якого відноситься ця дата ("літо", "осінь", "зима", "весна")


'''A function that determines the season by date.
The function receives a string in the format "day.month
  and should return a string with the corresponding season.'''

season_date = ["25.06", "12.01", "30.08", "01.11", "20.05"]

def season():

    winter = [date for date in season_date if date[3:5] == '01' or date[3:5] == '02' or date[3:5] == '12']
    print(winter)
    print("It's winter")
    spring = [date for date in season_date if date[3:5] == '03' or date[3:5] == '04' or date[3:5] == '05']
    print(spring)
    print("It's spring")
    summer = [date for date in season_date if date[3:5] == '06' or date[3:5] == '07' or date[3:5] == '08']
    print(summer)
    print("It's summer")
    automn = [date for date in season_date if date[3:5] == '09' or date[3:5] == '10' or date[3:5] == '11']
    print(automn)
    print("It's automn")


season()

# 2.Напишіть функцію "Тупий калькулятор", яка приймає два числових аргументи
# і строковий, який відповідає за операцію між ними (+ - / *).
# Функція повинна повертати значення відповідної операції (додавання, віднімання, ділення, множення),
# інші операції не допускаються. Якщо функція оримала невірний тип данних для операції
# (не числа) або неприпустимий (невідомий) тип операції вона повинна повернути None
# і вивести повідомлення "Невірний тип даних" або "Операція не підтримується" відповідно.

'''The "Dumb Calculator" function, which accepts two numeric arguments and
    a string, which is responsible for the operation between them (+ - / *)'''

def stupid_calc(num1, num2):

    operands = ['+', '-', '/', '*']

    for item in operands:
        try:
            if item == '+':
                print(num1 + num2)
            elif item == '-':
                print(num1 - num2)
            elif item == '/':
                print(num1 / num2)
            elif item == '*':
                print(num1 * num2)
        except TypeError:
            print("Невірний тип даних")

stupid_calc(7, 'f')

# 3.Напишіть докстрінг для обох функцій