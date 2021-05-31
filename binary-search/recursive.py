
def binary_search_recursive(list, target, left, right):
  if left > right:
    return False

  middle = (left + right) // 2
  print('Middle', list[middle])
  if (list[middle] == target):
    return True
  elif target < list[middle]:
    print('right')
    print(list[left:middle - 1])
    return binary_search_recursive(list, target, left, middle - 1)
  else:
    print('left')
    print(list[middle + 1:right])
    return binary_search_recursive(list, target, middle + 1, right)



numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 40 as an example

# [10, 20, 30, 40]

# [10, 20, 30]

# [20, 30, 40]

# [30, 40]



print(binary_search_recursive(numbers, 40, 0, len(numbers) - 1))