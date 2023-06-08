import fibo

print(fibo.fib(1000))
print(fibo.fib2(1000))

from fibo import fib, fib2

print(fib(1000))
print(fib2(1000))

from fibo import *
print(fib(1000))

import fibo as fib
print(fib.fib(1000))

from fibo.fibo import fib, fib2
print("Importing package...")
print(fib(1000))
print(fib2(1000))