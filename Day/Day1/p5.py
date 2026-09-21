#Concept:decorator is a python feature that allows you to modify the behavior of a function or class using @ symbol.
def my_decorator(func):
    def wrapper():
        print("before.")
        func()
        print("after.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!") 

say_hello()