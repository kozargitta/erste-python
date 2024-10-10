users = [
    {
        "id": 1,
        "first_name": "Rosalie",
        "last_name": "Pingston",
        "email": "rpingston0@ifeng.com",
    },
    {
        "id": 2,
        "first_name": "Darill",
        "last_name": "Taverner",
        "email": "dtaverner1@clickbank.net",
    },
    {
        "id": 3,
        "first_name": "Darryl",
        "last_name": "Wilkennson",
        "email": "dwilkennson2@uol.com.br",
    },
    {
        "id": 4,
        "first_name": "Raff",
        "last_name": "D'Aulby",
        "email": "rdaulby3@icio.us",
    },
    {"id": 5, "first_name": "Cherye", "last_name": "Clyma", "email": "cclyma4@nhs.uk"},
    {
        "id": 6,
        "first_name": "Vince",
        "last_name": "Vakhrushev",
        "email": "vvakhrushev5@paginegialle.it",
    },
    {"id": 7, "first_name": "Pattin", "last_name": "Orys", "email": "porys6@nhs.uk"},
    {
        "id": 8,
        "first_name": "Rawley",
        "last_name": "Yearnsley",
        "email": "ryearnsley7@joomla.org",
    },
    {
        "id": 9,
        "first_name": "Brigham",
        "last_name": "Spinige",
        "email": "bspinige8@cafepress.com",
    },
    {
        "id": 10,
        "first_name": "Townsend",
        "last_name": "Hacket",
        "email": "thacket9@netscape.com",
    },
]


def generate_id():
    # ids = [user["id"] for user in users]
    # return max(ids) + 1
    return max(user["id"] for user in users) + 1


def list_users():
    return users


def find_user(id):
    for user in users:
        if user["id"] == id:
            return user
    # return None


print(find_user(3))


def create_user(user):
    base_user = {"id": generate_id()}
    base_user.update(user)
    users.append(base_user)
    return users[-1]


print(
    create_user({"first_name": "John", "last_name": "Doe", "email": "johndoe@mail.com"})
)


def update_user(id, updated_user):
    user = find_user(id)
    if user:
        index = users.index(user)
        user.update(updated_user)
        users[index] = user
        # users[users.index(user)].update(updated_user)
        return users[index]


print(update_user(1, {"first_name": "Johnathan"}))


def delete_user(id):
    # if user exists by id, remove them
    user = find_user(id)
    # if user:
    #     users.remove(user)
    if user is not None:
        users.remove(user)
