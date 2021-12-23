from itertools import count

for el in count(int(input('Введите стартовое число: '))):
  print(el, end='')
  q = input()
  if q.lower() == 'q':
    print('Пока!')
    break
