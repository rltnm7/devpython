
class UserDetailResponse:
    def __init__(self, *, id, username, name, birthday, age):
        self.id = id
        self.username = username
        self.name = name
        self.birthday = birthday
        self.age = age

    def __eq__(self, other):
        if self.id != other.id:
            return False

        if self.username != other.username:
            return False

        if self.name != other.name:
            return False

        if self.birthday != other.birthday:
            return False

        if self.age != other.age:
            return False

        return True