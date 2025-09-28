def outer_function():
    var1 = "hello"
    print(var1)

    def inner_function():
        var2 = "world"
        print(var1, var2)

    def inner_function2():
        var3 = "welcome"
        print(var1,var3)


    inner_function2()
    inner_function()


outer_function()
