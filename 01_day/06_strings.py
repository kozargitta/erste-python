name = "Gáll Gergely"
print(name)
print(name[1])

# TypeError, str is immutable
# name[0] = "g"

name = "O'brian"
# name = 'O\'brian'
# cite = "\"cite\""
cite = '"cite"'

print("first line\nsecond line")
# print("""first line
# second line""")

first_name = "John"
last_name = "Doe"
age = 40
# old school way
full_name = first_name + " " + last_name
# old school way
sentence = (
    "My name is: " + first_name + " " + last_name + ", I'm " + str(age) + " years old."
)
print(sentence)

# better version
sentence = "My name is: {0} {1}, I'm {2} years old.".format(first_name, last_name, age)
print(sentence)

# best version
sentence = f"My name is: {first_name} {last_name}, I'm {age} years old."
print(sentence)

sentence = f"My name is: {first_name.upper()} {last_name.upper()}, I'm {age} years old."
print(sentence)

print(first_name.upper())
print("hello".upper())
print("hello" * 5)

# print("line\\nline\\nline\\nline")
print(r"line\nline\nline\nline")
