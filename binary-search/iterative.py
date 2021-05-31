def binary_search_iterative(list, target):
  left = 0
  right = len(list) - 1

  while (left <= right):
    center = (left + right) // 2
    if (list[center] > target):
      right = center - 1 # focus on the left side
    elif (list[center] < target):
      left = center + 1 # focus on the right side
    else:
      return target

  return None


numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(binary_search_iterative(numbers, 5))