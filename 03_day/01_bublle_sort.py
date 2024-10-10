# def bubble_sort(values):
#     for i in range(len(values)):
#         for j in range(len(values) - i - 1):
#             print(i, j)
#             if values[j] > values[j + 1]:
#                 values[j], values[j + 1] = values[j + 1], values[j]
#     return values


def advanced_bubble_sort(values):
    for i in range(len(values)):
        swapped = False
        for j in range(len(values) - i - 1):
            print(i, j)
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True
        if not swapped:
            break
    return values


print(advanced_bubble_sort([4, 3, 2, 1, 6, 5]))
print("---")
print(advanced_bubble_sort([1, 2, 3, 4, 5, 6]))


# abc = ["ödön", "Ödön", "öröm", "Őz", "űz", "álmos", "almos", "Űr"]
abc = ["odo", "Odo", "orom", "Oz", "uz", "almos", "almos", "Ur"]
abc.sort()
print(abc)
print("odo" == "Odo".lower())
