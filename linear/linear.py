
def linear_search(list, value):
  for i in range(len(list)):
    if list[i] == value:
      return list[i], i
  return -1



list = [1, 4, 6, 2, 16, 8, 20, 45]

print(linear_search(list, 20))
