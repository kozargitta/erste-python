for i in range(5):
    print(i)

# for ciklusváltozó in iterable:
#     ciklusmag

# ciklusváltozó = kezdőérték
# while feltétel:
#   ciklusmag
#   léptetés

i = 0
while i < 5:
    print(i)
    i += 1

while True:
    grade = input("Adj meg egy érdemjegyet: ")
    if grade.isdigit() and 1 <= int(grade) <= 5:
        print("Köszönöm a megadott érdemjegyet")
        break
    print("Hibás érdemjegy")

value = 0
if value:
    print("True")
