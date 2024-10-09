for i in range(5):
    print(i)

print("END")

for i in range(5, 10):
    print(i)

print("END")

for i in range(2, 10, 2):
    print(i, end=", ")

print("END")

for i in range(100, 0, -5):
    print(i, end=", ")

print("END")

yearly_salaries = [11_000, 22_300, 45_000, 35_800, 50_000]
for salary in yearly_salaries:
    print(salary)

for i in range(len(yearly_salaries)):
    print(f"index: {i}, value: {yearly_salaries[i]}")

for i, salary in enumerate(yearly_salaries):
    print(f"index: {i}, value: {salary}")

net_prices = [100, 200, 300, 400, 500]
gross_prices = []
standard_hungarian_vat_in_percent = 27

for net_price in net_prices:
    gross_prices.append(net_price * (1 + standard_hungarian_vat_in_percent / 100))

print(gross_prices)
