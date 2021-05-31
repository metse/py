# list comprehensions
words = 'The crazy thing about life is that you only live once'.split()
l = [word[0:1] for word in words]
# l = [len(word) for word in words]

# print(l)

# dict comprehensions
country_to_capital = { 'United Kingdom': 'London', 'Brazil': 'Brasilia', 'Morocco': 'Rabat', 'Sweden': 'Stockholm' }
capital_to_country = { capital: country for country, capital in country_to_capital.items() }

print(capital_to_country)