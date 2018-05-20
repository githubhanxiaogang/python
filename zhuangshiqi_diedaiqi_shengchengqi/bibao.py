# 在python中创建一个闭包可以归结为以下三点：
# 闭包函数必须有内嵌函数；
# 内嵌函数需要引用该嵌套函数上一级命名空间中的变量
# 闭包函数必须返回内嵌函数在python 中，函数对象有一个__closuew__属性，我们可以通过这个属性看看闭包的一些细节
# 从这里可以看到闭包的原理，当内嵌函数引用了包含它的函数（enclosing function）中的变量后，
# 这些变量会被保存在闭包函数的__closure__属性中，成为闭包函数本身的一部分； 也就是说，这些变量的生命周期会和闭包函数一样。
def npower():
    # 闭包函数npower(),内嵌函数power()
    n = 2
    def power(x):
        return x ** n
    return power

if __name__ == '__main__':
    f = npower()
    print(f(2))
    print(f.__closure__)
    print(f.__closure__[0].cell_contents)