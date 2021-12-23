from itertools import cycle

for el in cycle(input('Введите список, разделённый пробелом: ').split()):
  print(el, end='')
  q = input()
  if q.lower() == 'q':
    print('Пока!')
    break
