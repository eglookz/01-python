def f_gen(m):
  for n, el in enumerate(m):
    if m[n - 1] < m[n]:
      yield el

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f'Исходный список {my_list}')

# Один из вариантов формирования результирующего списка
# my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]

my_new_list = f_gen(my_list)
print(f'Новый список {list(my_new_list)}')
