import sys, numpy
import platform

print(platform.python_implementation())         # CPython

'''
Cpython use reference counts as main garbage collection mechanism.
Everything in python is a PyObject in C.

typedef struct _object {
    Py_ssize_t ob_refcnt;
    struct _typeobject *ob_type;
} PyObject;
'''
a = numpy.array([1.2,3.4])      # The reference object is the numpy array. 

print(sys.getrefcount(a))       # returrn 2
b = a
print(sys.getrefcount(a))       # return 3
del b
print(sys.getrefcount(a))       # return 2

print("-" * 65)

'''
Sometimes the reference counting will not work (data leakage).
Eg. Cyclical references.
Manually call the garbage collector with mark and sweep.
'''
class A(str):
    def __del__(self):
        print(self, 'has been deleted')

print(sys.getrefcount(A))       # 5
temp = A('temp')
temp.b = temp                   # Self reference.
print(sys.getrefcount(A))       # 6
del temp
print(sys.getrefcount(A))       # 6, reference count stays the same, __del__ method not called.

print("calling garbage collector")
import gc
gc.collect()
print(sys.getrefcount(A))       # 5, manually call the garbage collector.
