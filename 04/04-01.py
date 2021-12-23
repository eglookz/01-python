from sys import argv

_, hours, salary, bonus = argv
try:
    hours = int(hours)
    salary = int(salary)
    bonus = int(bonus)
    res = hours * salary + bonus
    print(f'заработная плата сотрудника  {res}')
    
except ValueError:
    print('Необходимо число!')
