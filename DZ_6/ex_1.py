"""
Программа запрашивает у пользователя пароль и записывает в переменную password.

Необходимо посчитать сложность пароля, где за каждую пройденную проверку пароль получает +1 балл к итоговой оценке, максимальное количество баллов - 5

Проверки:

Длина пароля больше или равно 8 символам
В пароле есть хотя бы одна цифра
В пароле есть хотя бы одна большая
В пароле есть хотя бы одна маленькая буква
В пароле есть хотя бы один спец символ (+, -, /, _, % и т.д. P.S. их на самом деле больше)
После всех проверок нужно вывести пользователю число - количество баллов за пароль, а так-же рекомендации по улучшению пароля.
"""
text = (input('Enter your password:'))

s = ".,:;!_*-+()/#%&@"

score = 0

print("Recommendation:")

if len(text) >= 8:
    score += 1
else:
    print('The minimum password length is 8')

for char in text:
    if char.isdigit():
        score += 1
        break
else:
    print('Use digits')

for char in text:
    if char.isupper():
        score += 1
        break
else:
    print('Use capital letters')

for char in text:
    if char.islower():
        score += 1
        break
else:
    print('Use lowercase letters')

for char in s:
    if char in text:
        score += 1
        break
else:
    print('Use special characters')


if score == 5:
        print('No recommendation ')

print('Passwor score', score)











