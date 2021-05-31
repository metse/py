acronyms = ['LOL', 'TBH', 'IDK', 'SMH']
expenses = [1, 2, 3, 4, 5]
# print last
# print(acronyms[len(acronyms) - 1])

acronyms.append('BFN')

# print(acronyms[len(acronyms) - 1])
total = 0
for exp in expenses:
  total += exp

# print(total)
# print(sum(expenses))

for year in range(2010, 2022, 2):
  print(year)