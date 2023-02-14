def cache_decorator(func):
    d = {}

    def inner(*args):
        try:
            return d[args]
        except KeyError:
            res = func(*args)
            d[args] = res
            return res

    return inner


@cache_decorator
def steps_to(stair):
    if stair == 1:
        return 1
    elif stair == 2:
        return 2
    elif stair == 3:
        return 4
    else:
        return (
                steps_to(stair - 3)
                + steps_to(stair - 2)
                + steps_to(stair - 1)
        )


@cache_decorator
def square_area(a: float) -> float:
    print(f'Вызвана функция square_area с аргументом {a} ')
    return a * a


print('Результат выполнения steps_to(50):', steps_to(50))
print('Результат выполнения steps_to(50):', steps_to(50))
print('Результат выполнения square_area(5):', square_area(5))
print('Результат выполнения steps_to(20):', steps_to(20))
print('Результат выполнения square_area(5):', square_area(5))
