# mutable, no indext, unique values, no ordered
x1 = {"a", "b", "c", "c"}
print(type(x1), x1)

# TypeError: 'set' object is not subscriptable
# print(x1[0])

x1.add("d")
print(x1)
x1.update({"e", "f"})
print(x1)
x1.remove("a")
print(x1)
# not raise error
x1.discard("x")
print(x1)

x1.pop()
print(x1)

numbers = [
    1,
    2,
    3,
    4,
    3,
    3,
    2,
    1,
    2,
    1,
    1,
]

unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print(unique_numbers)

unique_numbers = list(set(numbers))
print(unique_numbers)

x1 = {"a", "b", "c"}
x2 = {"b", "c", "d"}

print(x1.union(x2))  # x1 | x2
print(x1.intersection(x2))  # x1 & x2
print(x1.difference(x2))  # x1 - x2
print(x1.symmetric_difference(x2))  # x1 ^ x2
print(x1.issubset({"a", "b", "c", "d"}))  # x1 <= x2
print(x1.issuperset({"a", "b"}))  # x1 >= x2
print(x1.isdisjoint(x2))
