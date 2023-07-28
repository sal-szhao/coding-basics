'''
This file will include new PEP features in Python 3.10.
For each new python version, the overall performance will be improved.
'''

'''
Add match(switch) case function in Python.
'''
def match_case(color):
    match color:
        case "b":
            print("black")
        case "w":
            print("white")
        case _:
            print("other color")

'''
New context manager with parenthesis.
'''
def context_manager():
    with (
        open("foo.txt") as foo,
        open("baz.txt") as baz,
    ):
        print("file opened")

'''
Add strict arugment for zip, requiring the zipped lists to have equal length.
'''
def strict_zip():
    names = ['May', 'Mary', 'Ben']
    ages = [22, 26]

    # Normal zip will ignore the last element in names.
    result = zip(names, ages)
    print(list(result))

    # In strict mode, zip will raise an error if not equal length.
    result = zip(names, ages, strict=True)
    print(list(result))


'''
Better error messages showing where the error occurs.
'''
# print("Hello"
          
'''
Add explicit type alias because sometimes python cannot recognize 
whether it is an assignment or type declaration (for complicated type).
Add type abbreviations (& / |).
'''
from typing import TypeAlias
card_orgin = tuple[str, str]
card_alias: TypeAlias = tuple[str, str]

def square(number: int | float) -> int | float:
    # Check the type of number.
    print(number)
    # Check the type of card_alias.
    print(card_alias)


if __name__ == '__main__':
    import sys

    match len(sys.argv):
        case 1:
            print(globals())        # Print all the global names in the file.
        case 2:
            globals()[sys.argv[1]]()
        case 3:
            globals()[sys.argv[1]](sys.argv[2])
        