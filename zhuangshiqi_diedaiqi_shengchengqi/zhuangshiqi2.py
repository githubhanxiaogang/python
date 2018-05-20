# 返回函数被装饰的函数

def add_decorator(f):
    print("加法")
    return f

@add_decorator
def add_method(x,y):
    return x + y

print(add_method(2,3))