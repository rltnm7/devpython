import sys
sys.path.append("src")


def eq_users(left, right):
    return left.id == right.id and left.username == right.username \
        and left.name == right.name and left.birthday == right.birthday \
        and left.age == right.age
