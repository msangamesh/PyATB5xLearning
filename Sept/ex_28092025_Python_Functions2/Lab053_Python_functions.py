
def decorator1(func):
    def wrapper():
        print("inside decorator1")
        func()
    return wrapper()

def decorator2(func):
    def wrapper():
        print("inside decorator2")
        func()
    return wrapper()

# @decorator1
@decorator2
def greet():
    print(" greet hello")


