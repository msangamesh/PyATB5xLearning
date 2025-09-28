 # Annotations(Decorators)

def before_office(func):

    def wrapper():

        print("Get id card")
        func()
        print("Done for the day")
    return wrapper()


@before_office
def go_to_office():
     print("Go to office")

@before_office
def go_to_office2():
     print("get bike keys")



