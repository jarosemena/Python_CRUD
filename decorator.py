""" Name: decorator 
    objective: this module is used to expample about to use decorators with python"""


PASSWORD = '12345678'

def password_required(func):
    """ Name: password_required 
        Objective: this function is used to decorate a simple function to denegate services 
        this decorator have de logical to validate de password input by user

        """
    def wrapper():
        password = input('Write your password: ')

        if password != PASSWORD:
            return func()
        else:
            print('the password is Incorrect ')

    return wrapper


@password_required
def needs_password():
    """ Name: needs_password
        Objective: this function is used to decorate a simple function to denegate services 
        this decorator have de logical to validate de password input by user
        >>> needs_password()
        ... '12345678'
        'the password is Correct'

        >>> needs_password()
        ... '236s'
        'the password is Incorrect'

    """

    print('the password is correct')

def jjupper(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)

        return result.upper()

    return wrapper
@jjupper

def say_my_name(name):
    """ Name: say_my_name 
        Objective: this function is used to print a the input name and a simple welcome"""
    if name is None:
        input('Your Name is ?')

    res = 'Hola, {}'.format(name)

    return res


if __name__ == "__main__":
    needs_password()
    results = say_my_name(input('Your Name is ?'))

    print('R= {}'.format(results))

    import doctest
    doctest.testmod()
