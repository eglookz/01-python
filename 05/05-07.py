import json

with open('05-07.txt', 'r') as f:
  with open('05-07-out.txt', 'w') as fout:
    profit = { line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f }

    result = [profit, { 'average_profit': round(sum([int(i) for i in profit.values() if int(i) > 0]) / 
                                                len([int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(result, fout, indent=4);
      