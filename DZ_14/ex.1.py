from functools import lru_cache


# def decorating_function(user_function):
#     wrapper = _lru_cache_wrapper(user_function, maxsize, typed, _CacheInfo)
#     wrapper.cache_parameters = lambda: {'maxsize': maxsize, 'typed': typed}
#     return update_wrapper(wrapper, user_function)
#
#
# return decorating_function


@lru_cache
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


@lru_cache
def square_area(a: float) -> float:
    print(f'Вызвана функция square_area с аргументом {a} ')
    return a * a


print('Результат выполнения steps_to(30):', steps_to(30))
print('Результат выполнения steps_to(30):', steps_to(30))
print('Результат выполнения square_area(5):', square_area(5))
print('Результат выполнения steps_to(20):', steps_to(20))
print('Результат выполнения square_area(5):', square_area(5))
