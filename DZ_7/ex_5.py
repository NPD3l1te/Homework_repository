a =[]
for i in range(5):
    b = int(input('Введите число:'))
    a.append(b)
print(a)
c = []
for i in a:
    if i > 5:
        c.append(i)
print(c)
