from os import path, getcwd

print("getcwd:", getcwd())
print("__file__:", __file__)
print("abspath:", path.abspath(__file__))
print("dirname:", path.dirname(__file__))
print("basename:", path.basename(__file__))

# file_path = './files/file.txt'
file_path = path.join(path.dirname(__file__), "files", "file.txt")
