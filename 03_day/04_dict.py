# indexed by str, or tuple... uniqe values
user = {"name": "John Doe", "age": 33}
print(user["name"])

user["name"] = "Jane Doe"
print(user["name"])

user["job"] = "developer"
print(user)

user.update({"name": "Jack Doe", "hobby": "reading"})
print(user)

user.pop("hobby")
print(user)

for i in user:
    print(i)

print(user.keys())
print(user.values())
print(user.items())

for value in user.values():
    print(value)

for key, value in user.items():
    print(key, value)

# unpaking
name, age, job = user.values()
print(name, age, job)

# comprenhension
cart_net_prices = {"VGA": 500, "CPU": 1000, "RAM": 200}
cart_gross_prices = {k: v * 1.27 for k, v in cart_net_prices.items()}
print(cart_gross_prices)
