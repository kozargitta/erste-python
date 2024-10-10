number = 5
i = 2
# is_prime = True

while i <= number // 2:
    if number % i == 0:
        print("Not prime")
        break
    i += 1
else:
    print("Prime")

# if is_prime:
#     print("Prime")
# else:
#     print("Not prime")

# message = "Prime" if is_prime else "Not prime"
# print(message)
