import time

def decorator_time(func2):
    def decorator():
        start_time = time.time()
        print("start time",start_time)
        func2()
        end_time = time.time()
        print("End time",end_time)
        time_taken = end_time - start_time
        print("time taken", time_taken)

    return decorator()

def print_logs(func3):
    def wrapper():
        print("Starting logs")
        func3()
        print("Finished logs")

    return wrapper()



@decorator_time
@print_logs
def test_ui_1():
    print("Time taken by function 1")
    time.sleep(2)



# @decorator_time
# def test_ui_2():
#     print("Time taken by function 2")
#     time.sleep(5)