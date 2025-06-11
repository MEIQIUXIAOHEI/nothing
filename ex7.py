# 基本装饰器
def decorate(func):
    def inner():
        print("Start of function")
        func()
        print("End of function")
    return inner

@decorate
def say_hi():
    print("Hello there!")

say_hi()


# 带参数的装饰器
def repeat_times(times):
    def real_decorator(fn):
        def wrapped(*args, **kwargs):
            for _ in range(times):
                fn(*args, **kwargs)
        return wrapped
    return real_decorator

@repeat_times(3)
def welcome(user):
    print(f"Welcome, {user}!")

welcome("Alice")
