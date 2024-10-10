net_prices = [100, 200, 300, 400, 500]
standard_hungarian_vat_in_percent = 27
# gross_prices = []

# for net_price in net_prices:
#     gross_prices.append(net_price * (1 + standard_hungarian_vat_in_percent / 100))
# fmt: off
gross_prices = [net_price * (1 + standard_hungarian_vat_in_percent / 100) for net_price in net_prices]
# fmt: on
print(gross_prices)

numbes = [i for i in range(5, 101, 5)]
print(numbes)

# matrix = []
# for i in range(5):
#     row = []
#     for j in range(5):
#         row.append(j)
#     matrix.append(row)
matrix = [[j for j in range(5)] for _ in range(5)]

print(matrix)
# for row in matrix:
#     for item in row:
#         print(item)
flatten_matrix = [item for row in matrix for item in row]
print(flatten_matrix)

# this is NOT comprehension
numbers = list(range(1, 11))
print(numbers)
# this is comprehension
even_numbers = [number for number in numbers if number % 2 == 0]
