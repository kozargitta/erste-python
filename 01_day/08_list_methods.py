yearly_salaries = [100_000, 90_000, 85_000, 70_000, 55_000]
yearly_salaries[0] = 65_000
print(yearly_salaries)
# IndexError
# yearly_salaries[10] = 65_000

yearly_salaries.append(105_000)
print(yearly_salaries)

yearly_salaries.extend([44_000, 98_500])
print(yearly_salaries)

yearly_salaries.insert(1, 201_000)
print(yearly_salaries)

del yearly_salaries[0]
print(yearly_salaries)

yearly_salaries.remove(201_000)
print(yearly_salaries)

yearly_salaries.pop()
print(yearly_salaries)

print(yearly_salaries.count(55_000))

yearly_salaries.sort()
print(yearly_salaries)
yearly_salaries.sort(reverse=True)
print(yearly_salaries)

words = "Hello, my name is John Doe, and I'm dead.".split(" ")
print(words)
sentence = " ".join(words)
print(sentence)
