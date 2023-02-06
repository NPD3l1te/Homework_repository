def sum_range(start, end):
    if start > end:
        start, end = end, start
    c = 0
    for i in range(start, end + 1):
        c += i
    return c


a, b = map(int, input('Введите два числа от и до >>>').split())
print(sum_range(a, b))
