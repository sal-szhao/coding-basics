def scope_test():
    def do_local():
        print('do local')
        spam = "local spam"

    def do_nonlocal():
        print('do nonlocal')
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        print('do global')
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

## Directly assign a data attribute
scope_test.counter = 1
print(scope_test.counter)


## class variable and instance variable.
class Dog:
    
    tricks = []             # mistaken use of a class variable

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog()
e = Dog()
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)                # unexpectedly shared by all dogs



class Dog:

    def __init__(self):
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog()
e = Dog()
d.add_trick('roll over')
e.add_trick('play dead')
print('d tricks: ', d.tricks)
print('e tricks: ', e.tricks)


## Prioritization of instance variable.
class Warehouse:
   purpose = 'storage'
   region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)
print(w1.purpose, w1.region)


## Generator
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char, end='')
print()
