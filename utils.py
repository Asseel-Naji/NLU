def amazonify(*args, **kwargs):
    print("here comes the log writing function")

    def inner(func):

        # code functionality here
        print("here will be the before function") if kwargs['before'] else None
        func()
        print("here will be the after function") if kwargs['after'] else None

    # returning inner function
    return inner


