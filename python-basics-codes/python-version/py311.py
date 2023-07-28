'''
This file will include new PEP features in Python 3.10.
For each new python version, the overall performance will be improved.
'''

'''
Fine-grained error message.
'''
def fine_grained():
    x_list = [1, 2, 3, 4, 5]
    y_list = [2, 3, 0, 5, 6]
    print([x / y for x in x_list for y in y_list])

'''
Exception notes for adding additional error annotations for base exceptions.
Can add a list of exception notes.
'''
def exception_note():
    try:
        print(10 / 0)
    except ZeroDivisionError as e:
        e.add_note("Really divide zero?")
        e.add_note("Really divide zero?")
        e.add_note("Really divide zero?")
        raise

'''
Exception group enables to throw several exceptions in a group (tree exceptions).
except* allows for multiple except for one try and 
catches all the exceptions of a specific error type.
'''
def exception_group():
    try:
        raise ExceptionGroup(
            "eg",
            [
                ValueError('a'),
                TypeError('b'),
                ExceptionGroup(
                    "nested",
                    [TypeError('c'), KeyError('d')])
            ]
        )
    except* TypeError as e1:
        print(f'e1 = {e1!r}')
    except* Exception as e2:
        print(f'e2 = {e2!r}')

'''
TOML(Tom's Obvious Minimal Language) is a file format for configuration files,
serving as a substitution for JSON / DICT format.
Python3.11 support parsing toml format into dict.
'''
def toml_parse():
    import tomllib

    with open("settings.toml", "rb") as f:
        data = tomllib.load(f)
    
    print(data)

'''
Self type is a simple and intuitive way to annotate methods 
that are returning an instance of the class.
'''
from typing import Self
class MyClass:
    def set_parameter(self, parameter: str) -> Self:
        self.name = parameter
        return self

def self_type():    
    my_class = MyClass()
    new_class = my_class.set_parameter("Jack")
    print(new_class.name)


'''
Add StrEnum and auto functions for easier implementation of string enumeration class.
auto() will automatically assign the enumeration type name as the value of the type. 
'''
from enum import StrEnum, auto
class MyColor(StrEnum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

def str_enum():
    print(MyColor.RED.name)
    print(MyColor.RED.value)



if __name__ == '__main__':
    import sys

    match len(sys.argv):
        case 1:
            print(globals())        # Print all the global names in the file.
        case 2:
            globals()[sys.argv[1]]()
        case 3:
            globals()[sys.argv[1]](sys.argv[2])