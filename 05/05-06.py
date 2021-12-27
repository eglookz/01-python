import re

def extract_number(data):
  data = re.findall('\d+', data)
  result = data[0] if len(data) > 0 else 0
  return result

subj = {}
with open('05-06.txt', 'r') as f:
  for line in f:
    subject, lect, pract, labs = line.split()
    subject = subject[:-1]
    lect = extract_number(lect)
    pract = extract_number(pract)
    labs = extract_number(labs)
    
    subj[subject] = int(lect) + int(pract) + int(labs)
  print(f'Общее количество часов по предмету:\n {subj}')
