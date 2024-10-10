grade = input("Adj meg egy érdemjegyet: ")

# if grade == "1":
#     print("Elégtelen")
# elif grade == "2":
#     print("Elégséges")
# elif grade == "3":
#     print("Közepes")
# elif grade == "4":
#     print("Jó")
# elif grade == "5":
#     print("Jeles")
# else:
#     print("Hibás érdemjegy")

if grade.isdigit():
    grade = int(grade)

    if grade == 1:
        print("Elégtelen")
    elif grade == 2:
        print("Elégséges")
    elif grade == 3:
        print("Közepes")
    elif grade == 4:
        print("Jó")
    elif grade == 5:
        print("Jeles")
    else:
        print("Hibás érdemjegy")
else:
    print("Nem számot adtál meg")
