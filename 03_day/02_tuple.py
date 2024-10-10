rgb_color = (255, 0, 0)

print(rgb_color.count(255))
print(rgb_color.index(255))
print(rgb_color[0])

# TypeError
# rgb_color[0] = 0

# rgb_color = (1, 2, 3)
# rgb_color = "kiskutyafule"

# fmt: off
one_item_tuple = (1, )
print(type(one_item_tuple))

# unpaking works, slicing works

# fmt: on
def user_factory(first_name, last_name, age):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    age = int(age)
    return first_name, last_name, age


print(type(user_factory("john", "doe", "33")))

user = (12, "John Doe")
query = f"SELECT * FROM users WHERE id ={user[0]}"
