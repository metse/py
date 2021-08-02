f = open('test.txt', mode='rt', encoding='utf-8')

try:
  f = open('test.txt', mode='rt', encoding='utf-8')
  for i in f.readlines():
    print(i)
finally:
  f.close()