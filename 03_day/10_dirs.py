from os import path, mkdir, chdir, rename, rmdir, listdir

# mkdir(path.join(path.dirname(__file__), "new_dir"))
# print(listdir(path.join(path.dirname(__file__))))
# src = path.join(path.dirname(__file__), "new_dir")
# dest = path.join(path.dirname(__file__), "new_dir2")
# src = path.join(path.dirname(__file__), "new_dir2")
# dest = path.join(path.dirname(__file__), "files", "new_dir")
# rename(src, dest)
# rmdir(path.join(path.dirname(__file__), "files", "new_dir"))

chdir(path.join(path.dirname(__file__), "files"))
mkdir("new_dir")
