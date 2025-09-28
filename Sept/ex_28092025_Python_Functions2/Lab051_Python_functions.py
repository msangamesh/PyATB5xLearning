

def add_before_and_after_Ui_test(func):

    def wrapper():
        print("Before UI test")
        print("Start browser")
        func()
        print("After UI test")
        print("End browser")


    return wrapper()


@add_before_and_after_Ui_test
def test_ui():
    print("will test the UI")