
class UserResponse:
    def __init__(self, *, id, username):
        self.id = id
        self.username = username

    def __eq__(self, other):
        if self.id != other.id:
            return False

        if self.username != other.username:
            return False

        return True
