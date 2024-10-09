age = 39
age_copy = age

print("age", age)
print("age_copy", age_copy)
print("age id", id(age))
print("age_copy id", id(age_copy))

age = 18
print("age", age)
print("age_copy", age_copy)
print("age id", id(age))
print("age_copy id", id(age_copy))

yearly_salaries = [10_000, 20_000, 30_000]
yearly_salaries_copy = yearly_salaries
yearly_salaries.append(40_000)
yearly_salaries_copy.append(50_000)
yearly_salaries = ["John", "Jane", "Johnny"]

print("yearly_salaries", yearly_salaries)
print("yearly_salaries id", id(yearly_salaries))
print("yearly_salaries_copy", yearly_salaries_copy)
print("yearly_salaries_copy id", id(yearly_salaries_copy))

numbers = [1, 2, 3, 4, 5]
numbers_real_copy = numbers.copy()
print(id(numbers), id(numbers_real_copy))
