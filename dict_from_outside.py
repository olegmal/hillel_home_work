
# 3.є url https://dummyjson.com/users  (100 сторінок) вивести в консоль
# середній вік чоловіків з Brown волоссям, а також сформувати список людей,
# що проживають в місті Louisville
# обовязково прикріпити requirements.txt

import requests
from pprint import pprint

response = requests.get("https://dummyjson.com/users?limit=100")
print(response)
data = response.json()
users = data.get('users', [])
# pprint(users)



total_years = 0
count_brown_hair = 0

for user in users:
    if user['hair'].get('color').lower() == 'brown':
        count_brown_hair += 1
        years = user.get('age', 0)
        total_years += years
print(count_brown_hair)
print(total_years)
print(f"Середній вік чоловіків з коричневим волоссям: {total_years / count_brown_hair}")


# Люди з Луісвілля:

count = 0

for user in users:
    if user['address'].get('city', 0) == 'Louisville':
        count += 1
        print(count)


