def amazonify(*args, **kwargs):
    print("here comes the log writing function")

    def inner(func):

        # code functionality here
        print("here will be the before function")
        func()
        print("here will be the after function")

    # returning inner function
    return inner


