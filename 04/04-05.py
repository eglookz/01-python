from functools import reduce

def my_func(el1, el2):
    return el1 * el2

_list = range(100, 1001, 2)
print(f'Список чётных чисел: {list(_list)}')
print(f'Результат перемножения всех элементов списка: {reduce(my_func, _list)}')
