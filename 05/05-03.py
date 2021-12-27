with open('05-03.txt', 'r') as f:
  avg = []
  poor = []
  employees = f.read().split('\n')
  for employee in employees:
    employee = employee.split()
    if int(employee[1]) < 20000:
      poor.append(employee[0])
    avg.append(employee[1])
print(f'Оклад меньше 20000 {poor}, средний оклад {sum(map(int, avg)) / len(avg)}')
