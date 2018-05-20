# 装饰器是可调用的对象，其参数是另一个函数（被装饰的函数），装饰器可以处理被装饰的函数，然后把它返回，
# 也可以将其替换成另一个函数或可调用对象
# 它可以让被装饰的函数在不需要做任何代码变动的前提下增加额外的功能， 被装饰的函数当作参数传入，装饰器返回经过修饰后函数的名字；
#  内层函数（闭包）负责修饰被修饰函数。从上面这段描述中我们需要记住装饰器的几点属性，以便后面能更好的理解
#
# 实质： 是一个函数
# 参数：被装饰函数名
# 返回：返回一个函数（被装饰的函数或者另一个函数）
# 作用：为已经存在的对象添加额外的功能


def deco(func):
    def inner():
        print("running inner")
    return inner

@deco
def target():
    print("running target()")


if __name__ == '__main__':
    target()

# def deco(func):
#     def inner():
#         print("running inner()")
#     return inner
#
#
# def target():
#     print('running target()')
#
#
# if __name__ == "__main__":
#     target = deco(target)
#     target()
