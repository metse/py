def gen123():
  print('About to pass 1')
  yield 1
  print('About to pass 2')
  yield 2
  print('About to pass 3')
  yield 3
  print('About to return')

g = gen123()

next(g)
# next(g)
print(next(g))
print(next(g))


