def factorial(num):
  total = 1
  for i in range(1, num + 1):
    yield f'{i}! = {total}'
    total *= i + 1

for el in factorial(int(input('Введите число для высичления факториала: '))):
  print(el)
