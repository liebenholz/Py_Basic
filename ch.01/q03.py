import functools as ft

def add(x, y):
    return x + y

def outer(x):
    def inner(y):
        return x + y
   return inner

ft.partial(add, x)

