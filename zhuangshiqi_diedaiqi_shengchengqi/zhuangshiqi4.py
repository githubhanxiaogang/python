def out_f(arg):
    print("out_f" + arg)
    def decorator(func):
        def inner():
            func()
        return inner
    return decorator

@out_f('123')
def func():
    print("hello word")


if __name__ == '__main__':
    func()