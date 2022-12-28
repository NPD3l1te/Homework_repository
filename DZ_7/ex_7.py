text = input('Введите текст:')
print('Количество цифр:')
count = 0
for i in text:
    if i.isdigit():
        count += 1
else:
    print()
print(count)


