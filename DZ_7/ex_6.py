n = int(input('hhh'))
a = []
for i in range(n):
    number = int(input('Введите число:'))
    a.append(number)
print(a)

min = a[0]
max = a[0]

for i in a:
    if i > max:
        max = i
    if i < min:
        min = i
print(max)
print(min)



