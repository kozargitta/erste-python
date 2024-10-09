# indexed, mutable, can contain duplicated values, can store any types of data
# yearly_salaries = [100000, 90000, 85000, 70000, 55000, True, None, 55000, [1, 2, 3]]

yearly_salaries = [100_000, 90_000, 85_000, 70_000, 55_000]
# print(type(yearly_salaries[0]))

print(yearly_salaries[0])
yearly_salaries[0] = 110_000
print(yearly_salaries)
print(type(yearly_salaries))

# operators
print([1, 2, 3] + [3, 4, 5])
print([1, 2, 3] * 3)
print(10 in [10, 20, 30])
