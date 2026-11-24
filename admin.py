users = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"},
    {"name": "Charlie", "role": "admin"},
    {"name": "David"},
    {"name": "Eve", "role": "moderator"}
]
def admin():
    for user_name in users:
        try:
            if(user_name['role'])=="admin":
                print(user_name['name'])
        except KeyError:
            continue
admin()