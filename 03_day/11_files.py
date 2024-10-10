from os import chdir, path

chdir(path.join(path.dirname(__file__), "files"))

with open("file.txt", "r") as file:
    print(file.read())
    file.seek(0)
    # print(file.readline())
    # print(file.readlines())
    # for line in file:
    #     for char in line:
    #         print(char)

# with open("file.txt", "w") as file:
#     content = ["Hello", "World", "Python"]
# for line in content:
#     file.write(line + "\n")
# file.write("\n".join(content))

with open("file.txt", mode="a") as file:
    file.write("\nNew content")
