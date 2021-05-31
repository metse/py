# m = [1, 2, 3]

# def append(k):
#   k.append(4)
#   print('k =', k)

# append(m)

# print(m)

# def add_spam(menu=[]):
#   menu.append('spam')
#   return menu

# print(add_spam())
# print(add_spam())
t = (84, 23, 45, 123, 456, 12, 6)

def min_max(t):
  return min(t), max(t)

lower, upper = min_max(t)

# print(lower)
# print(upper)

a = 'jelly'
b = 'bean'

a, b = b, a # swap
list = [1, 2, 3, 4, 5, 6, 7]
# print('a =', a)
# print('b =', b)

print('unforgetable'.partition('forget'))

word = ['the', 'quick', 'brown', 'fox', 'jumps', 'somewhere']
print(word.count('fox'))
print(7 in list)