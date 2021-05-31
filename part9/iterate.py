# iterable = ['Spring', 'Summer', 'Winter', 'Autumn']
# iterator = iter(iterable)

def first(iterable):
  iterator = iter(iterable)
  try:
    return next(iterator)
  except StopIteration:
    raise ValueError('Iterable is empty')

first(['Spring', 'Summer', 'Winter', 'Autumn'])
first(['Spring', 'Summer', 'Winter', 'Autumn'])
first(['Spring', 'Summer', 'Winter', 'Autumn'])
first(['Spring', 'Summer', 'Winter', 'Autumn'])
print(first(['Spring', 'Summer', 'Winter', 'Autumn']))