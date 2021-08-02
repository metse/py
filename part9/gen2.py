def take(count, iterable):
  counter = 0
  for item in iterable:
    if counter == count:
      return
    counter += 1
    # print('Adding', item)
    yield item

def distinct(iterable):
  seen = set()
  for item in iterable:
    if item in seen:
      continue
    yield item
    seen.add(item)

t = take(3, [3, 6, 6, 2, 1, 1])
for i in t:
  print(i)

def run_pipeline():
  items = [3, 6, 6, 2, 1, 1]
  for item in take(4, list(distinct(items))): # list before takes does it's work
    print(item)


# run_pipeline()