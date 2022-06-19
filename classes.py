from flask_login import UserMixin

from connections import DB


class User(DB.Model, UserMixin):

    """
    Class for handling the users for the web app; connects to the database and utilizes the flask_login library.
    """

    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    user = DB.Column(DB.String(), unique=True)
    hash = DB.Column(DB.String())
    user_id = DB.Column(DB.Integer(), unique=True, primary_key=True)
    permissions = DB.Column(DB.String())
    email = DB.Column(DB.String())

    def __init__(self, user, _hash, permissions, user_id, email):
        self.user = user
        self.hash = _hash
        self.user_id = user_id
        self.permissions = permissions
        self.email = email

    def __repr__(self):
        return self.user

    def can_login(self, password):
        return self.password == password

    def is_active(self):
        return True

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.user_id

    def get_permissions(self):
        li = self.permissions
        li = li.strip('[]').split(', ')
        return li
