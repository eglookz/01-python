def f_gen(m):
  for n in range(1, len(m)):
    if m[n] > m[n - 1]:
      yield m[n]

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f'Исходный список {my_list}')

# Один из вариантов формирования результирующего списка
# my_new_list = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]

my_new_list = f_gen(my_list)
print(f'Новый список {list(my_new_list)}')
