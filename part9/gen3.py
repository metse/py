million_squares = (x*x for x in range(1, 1000000))
print(list(million_squares)[-10:])


# calculate sum
sum(x*x for x in range(1, 1000001))