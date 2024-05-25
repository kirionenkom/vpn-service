from flask_login import UserMixin

from database import get_user
from login_manager import login_manager


class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

    @staticmethod
    def get(user_id):
        user_data = get_user(user_id)
        if user_data is None:
            return None
        return User(user_data[0], user_data[1])


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)