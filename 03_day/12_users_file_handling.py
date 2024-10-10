from os import path, chdir

chdir(path.join(path.dirname(__file__), "files"))


def read_users(file_path):
    with open(file_path, "r") as file:
        users = []
        for line in file:
            id, fist_name, last_name, email = line.rstrip().split(";")
            users.append(
                {
                    "id": int(id),
                    "first_name": fist_name,
                    "last_name": last_name,
                    "email": email,
                }
            )
    return users


print(read_users("users.csv"))


def append_user(file_path, user):
    with open(file_path, "a") as file:
        # user_line = "\n"
        # user_line += str(user["id"]) + ";"
        # user_line += user["first_name"] + ";"
        # user_line += user["last_name"] + ";"
        # user_line += user["email"]
        # file.write(user_line)

        user_line = "\n" + ";".join(str(value) for value in user.values())
        file.write(user_line)


append_user(
    "users.csv",
    {"id": 200, "first_name": "John", "last_name": "Doe", "email": "jd@gmail.com"},
)
