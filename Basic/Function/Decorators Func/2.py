def user_name(func):
    def inner():
        user_msg=func()
        return user_msg.upper()
    return inner


@user_name
def name():
    return "sk"
print(name())