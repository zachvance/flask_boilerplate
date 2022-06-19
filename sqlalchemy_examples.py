from werkzeug.security import generate_password_hash

from classes import User
from connections import DB


def add_user(user_id, username, password, permissions, email) -> None:
    """
    Adds a user to the database.
    ...
    :return: None
    :rtype: None
    """

    _hash = generate_password_hash(password)
    user = User(username, _hash, permissions, user_id, email)
    DB.session.add(user)
    DB.session.commit()
    print("User added.")


def add_users():
    add_user("1", "admin", "admin", "[perm1, perm2]", "email@example.com")
    add_user("2", "user1", "password", "[perm2]", "user1@example.com")


def query_test():
    for user in User.query.all():
        print(user.user, user.get_permissions(), user.hash)

    user = User.query.filter(User.email == "user1@example.com").first()
    user.set_password("pw")
