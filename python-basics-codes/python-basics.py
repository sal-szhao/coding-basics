# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Passing system arguments.
import sys

if sys.argv and len(sys.argv) > 3:
    print('sys.argv: ', sys.argv)
    print('sys.argv[0]: ', sys.argv[0])
    print('sys.argv[1]: ', sys.argv[1])
    print('sys.argv[1]: ', sys.argv[2])

## Print multiple lines.
print('''
Usage: thingy [OPTIONS]
    -h                        Display this usage message
    -H hostname               Hostname to connect to
''')

## Print all list elements.
l = ['a', 'b', 'c']
print(*l)
print('-'.join(l))

## Function pass by value
a = 5
def alter(a):
    a = 4
print(a)

## Input from cmd.
name = input('Please enter your name: ')
print(name)

## Define functions.
a = 1

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

## keyword arguments
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot('a thousand', state='pushing up the daisies')

# # Not working (position arguments after keyword arguments)
# parrot(voltage=5.0, 'dead')

## * and ** formal parameters.

def cheeseshop(*positions, **keywords):
    for pos in positions:
        print(pos)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# Automatic annotations for the input and output of the functions.
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)

f('spam')


## map and lambda function
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
print(list(map(lambda x, y: x + y, numbers1, numbers2)))


## Some minor usage.
list1 = [1, 2]
list2 = [3, 4]
list1.extend(list2)
del(list1[:])
print(list1)

## zip function.
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]
print(list(zip(names, ages)))

## Tuple nesting
t = 12345, 54321, 'hello!'
u = t, (1, 2, 3, 4, 5)
print(u)

## Exceptions chaining
try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")
finally:
    print('Goodbye, world!')