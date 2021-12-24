with open('05-02-sample.txt', 'r') as f:
  content = f.readlines()
  print(f'Количество строк: {len(content)}')

  print('*' * 50)

  print('Количество слов в строке:')
  print('# строки\tКоличество слов')
  for idx, line in enumerate(content):
    words = line.split()
    print(f'{idx + 1}\t\t\t{len(words)}')

  f.close()
