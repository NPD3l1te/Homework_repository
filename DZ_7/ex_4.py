n = int(input('hhh'))
a = []
for i in range(n):
    number = int(input('Введите число:'))
    a.append(number)
a.sort(reverse=True)
print(a)

