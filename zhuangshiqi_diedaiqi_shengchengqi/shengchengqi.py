# 1.生成器函数生成器是一种用函数语法定义的迭代器，调用生成器函数返回一个迭代器yield语句挂起生成器函数
# 并向调用者发送一个值，迭代器的__next__继续运行函数。

L = [[1,2],[3,4],[5,]]

def flat(L):
  for sublist in L:
      for e in sublist:
          yield e

# for num in flat(L):
#     print(num)

def gen():
    for i in range(10):
        x = (yield i)
        print('hanxiaogang',x)

g = gen()
next(g)
print(g.send(11))
print(g.send(22))

