with open('test.txt', 'w', encoding='utf-8') as f:
  while True:
    line = input('Введите текст: ')
    if not line:
        break
    print(line, file=f)
f.close()

print('*' * 50)

with open('test.txt', 'r') as f:
  content = f.readlines()
  for line in content:
    print(line, end='')
  f.close()
