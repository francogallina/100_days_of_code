def loggin_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__} with parameters {args}")
        print(f"The result is {function(args[0], args[1])}")
    return wrapper

@loggin_decorator
def suma(n1, n2):
    return n1+n2

suma(1,4)
