# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
# 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
# RecursionError: maximum recursion depth exceeded 递归异常，超过最大递归深度
#  阶乘： n的阶乘为n * (n-1) * (n-2) * ... * 1
# x的n次幂 等于x 的n-1次幂乘x，x的0次幂等于1
# 练习：取出n层嵌套列表里的所有元素 提示判断一个元素i是否是list 使用isinstance(i,list)函数
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def power(x,n):
    if n ==0:
        return 1
    else:
        return x * power(x , n - 1)


def recu_list(L):
    for i in L:
        if isinstance(i ,list):
            recu_list(i)
        else:
            print(i)

if __name__ == "__main__":

    print(factorial(5))
    print(power(2,6))
    L =[1,[2,[3,[4,5]]]]
    recu_list(L)
