def mutable():
    '''
    Mutable variable and immutable variable.
    Alter a mutable variable is actually creating a new variable and assigning a new address.
    Alter an immutable variable will not change the address.
    '''
    x = 10
    print(id(x))
    x += 1
    print(id(x))

    # String is an immutable variable.
    x = "a"
    print(id(x))
    x += "b"
    print(id(x))

    x = [1, 2]
    print(id(x))
    x.append(3)
    print(id(x))

def equal():
    '''
    == will only check whether the values are equal.
    is will check whether the id of the variables are equal.
    '''
    # Immutable variables.
    a = 123
    b = 123
    print(id(a), id(b), a == b, a is b)

    a = "some info"
    b = "some info"
    print(id(a), id(b), a == b, a is b)

    # Mutable variables.
    a = [1, 2]
    b = [1, 2]
    print(id(a), id(b), a == b, a is b)

def encode():
    '''
    Unicode can transform and be transformed into different kinds of encodings.
    '''
    x = "上"    # By default, string in python is stored in unicode.
    res = x.encode("utf-8")     # Unicode transformation format is often used when it comes to disk storage.
    print(res)
    print(res.decode("utf-8"))

def closure():
    '''
    The advantage of closure function is that it can avoid repeatedly passing the arguments.
    '''
    def outer_function(x):
        def inner_function(y):
            return x * y
        return inner_function

    closure = outer_function(10)
    result1 = closure(5)
    result2 = closure(6)
    result3 = closure(19)
    print(result1, result2, result3)


def iterator():
    '''
    Iterator can save memory by not having read all the data at once.
    But it will hard to get the length of the data or coming back to the previous data.
    '''
    list = [1, 2, 3]
    i = iter(list)
    print(next(i))
    print(next(i))
    print(next(i))

if __name__ == '__main__':
    import sys

    match len(sys.argv):
        case 1:
            print(globals())        # Print all the global names in the file.
        case 2:
            globals()[sys.argv[1]]()
        case 3:
            globals()[sys.argv[1]](sys.argv[2])
