yearly_salaries = [
    10_000,
    20_000,
    30_000,
    40_000,
    50_000,
    60_000,
    70_000,
    80_000,
    90_000,
    100_000,
]

print(yearly_salaries[0])
print(yearly_salaries[2:5])
print(yearly_salaries[2:])
print(yearly_salaries[:5])
print(yearly_salaries[2:9:2])
print(yearly_salaries[::2])
print(yearly_salaries[::-2])
print(yearly_salaries[-1])

yearly_salaries_copy = yearly_salaries[:]
print(yearly_salaries_copy)
new_salaries = [22_000, 33_000, 44_000]
print(yearly_salaries_copy)
yearly_salaries_copy[2:5] = new_salaries
print(yearly_salaries_copy)
