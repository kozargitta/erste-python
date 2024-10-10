# first_name = "John"
# last_name = "Doe"
# age = 33

first_name, last_name, age = "John", "Doe", 33
print(first_name, last_name, age)

# data swapping
a = 10
b = 20

# tmp = a
# a = b
# b = tmp
a, b = b, a

abc = "abcdefghijkl"
a, b, c, *others = abc
print(a, b, c, others)

yearly_salaries = [
    11_000,
    35_800,
    50_000,
    22_300,
    45_000,
]
yearly_salaries.sort()
low, *middle, high = yearly_salaries
print(low, middle, high)

net_prices = [
    500,
    100,
    200,
    300,
    400,
]
# feladat: adott egy lista, amit integereket tartalmaz
# távolítsd el a legkisebb és legnagyobb elemet,
# feltételezheted, hogy a lista legalább 3 elemet tartalmaz, és nincsenek duplikáiciók,
# a maradéknak számítsd ki az átlagát, és mentsd el egy average változóba

net_prices.sort()
low, *middle, high = net_prices
# summa = 0
# for net_price in middle:
#     summa += net_price
# average = summa / len(middle)
average = sum(middle) / len(middle)
