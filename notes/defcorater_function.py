def decorator(func):
    def wrapper():
        print("before calling fucntion")
        func()
        print("affter fucntion")
    return wrapper
@decorator
def greet():
    print("hello world")
greet()