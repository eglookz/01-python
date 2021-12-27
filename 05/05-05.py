from random import randint

with open('05-05.txt', 'w+') as f:
  rand_list = [randint(1, 100) for _ in range(100)]
  f.writelines(' '.join(map(str, rand_list)))

  print('Сумма элементов списка:', sum(map(int, rand_list)))
