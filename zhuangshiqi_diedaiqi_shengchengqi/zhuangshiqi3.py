# 调用被装饰函数时,参数传递给返回的函数，所以wrap的参数要与被装饰函数一致，或者写成wrap(*arg, **dict)

def add_decorator(f):
    def wrap(x,y):
        print("加法")
        return f(x,y)
    return wrap


def add_method(x,y):
    return x +y

if __name__ == '__main__':
    print(add_method(2,3))