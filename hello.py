def calculateTax(amount, tax):
  return amount + amount * tax

# amount = input('Amount spent?\n')
# result = calculateTax(float(amount), 0.05)

# print('Total is ' + str(result))


age = int(input('How old are you?\n'))

decade = age // 10
year = age % 10

print('You are ' + str(decade) + ' decades and ' + str(year) + ' years old.')