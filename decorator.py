
PASSWORD = '12345678'

def password_required(func):
    def wrapper():
        password = input('Write your password: ')

        if password == PASSWORD:
            return func()
        else:
            print('the password is Incorrect ')

    return wrapper
@password_required

def needs_password():
    print('the password is correct')

def jjupper(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)

        return result.upper()

    return wrapper
@jjupper

def say_my_name(name):
    res = 'Hola, {}'.format(name)

    return res


if __name__ == "__main__":
#    password_required(needs_password())

    results = say_my_name(input('Your Name is ?'))

#    results = say_my_name(input('your Name is ?'))
    print('R= {}'.format(results))


