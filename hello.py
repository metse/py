def calculateTax(amount, tax):
  return amount + amount * tax


age = int(input('How old are you?\n'))

decade = age // 10
year = age % 10

print('You are ' + str(decade) + ' decades and ' + str(year) + ' years old.')