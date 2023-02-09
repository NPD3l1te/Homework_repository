import time


def cache_decorator(func):
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(time.time() - start)
        return res

    return inner()


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


def square_area(a: float) -> float:
    print(f'Вызвана функция square_area с аргументом {a} ')
    return a * a


print('Результат выполнения steps_to(20):', steps_to(20))
print('Результат выполнения steps_to(20):', steps_to(20))
print('Результат выполнения square_area(5):', square_area(5))
print('Результат выполнения steps_to(30):', steps_to(30))
print('Результат выполнения square_area(5):', square_area(5))
