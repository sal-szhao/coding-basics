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

'''
MRO (Method Resolution Order): depth-first-search then breadth-first-search 
in multiple inheritance.
'''
class A(object): pass
class B(A): pass
class C(A): pass
class D_0(B, C): pass
class D_1(B, C): pass
class E_0(D_0): pass
class E_1(D_1): pass
class F(E_0, E_1): pass

print(F.__mro__)

'''
super() method allows child to access the methods in parents.
Search order follows MRO.
'''
class People:
    school='清华大学'     
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
 
class Teacher(People):
    def __init__(self, name, sex, age, title):
        super().__init__(name, sex, age)
        self.title = title
    
obj = Teacher('lili', 'female', 28, '高级讲师')
print(obj.name, obj.sex, obj.age, obj.title)

'''
Abstract class cannot be instantiated.
Abstract method must be implemented in children class.
'''
import abc

class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        pass

cat=Cat()

'''
class can define methods on a class level using `@classmethod`.
class can define static methods that are irrelevant to the class or instance,
not need to pass in `self` variable.
'''
class MyClass:
    class_variable = 10

    @classmethod
    def update_class_variable(cls, new_value):
        cls.class_variable = new_value

    @staticmethod
    def static():
        print("Using static method.")

example = MyClass()
print("Before update:", example.class_variable)
MyClass.update_class_variable(15)
example = MyClass()
print("After update:", example.class_variable)
example.static()

'''
Some built-in methods in the class.
'''
class People:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def __str__(self):
        return '<Name:%s Age:%s>' % (self.name, self.age)
    
    def __del__(self):
        print("People removed.")
 
p = People('lili', 18)
print(hasattr(p, "name"))
print(getattr(p, "age", None))
print(p)
del p

'''
Default metaclass for a python class is type.
class_name='StanfordTeacher', class_bases=(object,), class_dic(namespace)
will be passed into metaclass to generate a python class.
By default the base class is `object`.
Eg. metaclass can be used to do validation for a class...
'''
class Mymetaclass(type):
    def __init__(self, *args, **kwargs):
        print(args)
        if not args[0].istitle():
            raise NameError("Invaliated class name.")
     
class Chinese(object, metaclass=Mymetaclass):
    def walk(self):
        print('Jesus is walking.')

## Generator
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char, end='')
print()
