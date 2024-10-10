def greeting(name, age):
    print(f"Hello {name}! You are {age} years old.")


greeting("John", 33)
print(greeting("Jane", 30))

# print(dir(__builtins__))


def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


print(even_or_odd(5))
print(even_or_odd(6))


def calculate_gross_price(net_price, vat_in_percent=27):
    return net_price * (1 + vat_in_percent / 100)


print(calculate_gross_price(100))
print(calculate_gross_price(200))
print(calculate_gross_price(1000, 5))
print(calculate_gross_price(vat_in_percent=27, net_price=50))


def add_item_to_basket(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket


print(add_item_to_basket("VGA"))
print(add_item_to_basket("CPU"))
print(add_item_to_basket("Cooler"))

global_variable = "global"
print(global_variable)


def log_global_variable():
    local_variable = "local"
    print(global_variable)
    print(local_variable)
    return local_variable


log_global_variable()
result = log_global_variable()
print(result)

my_variable = "global"


def my_function():
    global my_variable
    my_variable = "local"
    print(my_variable)


print("----------------")
my_function()
print(my_variable)


def add_item_to_cart(item, cart):
    # cart = []
    cart.append(item)
    # return cart


my_cart = ["VGA", "CPU"]
print(add_item_to_cart("Cooler", my_cart))
print(my_cart)

# rekurzió


def gcd_loop(a, b):
    while b:
        # 10, 15
        # 15, 5
        # 5, 0
        a, b = b, a % b
    return a


print(gcd_loop(10, 15))


def gcd_rec(a, b):
    return a if b == 0 else gcd_rec(b, a % b)


print(gcd_rec(10, 15))
