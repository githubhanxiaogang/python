#迭代的意思是重复做一些事很多次，for循环就是一种迭代，列表，字典，元组，都是可迭代对象，
# 实现__iter__方法的对象都是可迭代的对象。iter返回一个迭代器，所谓迭代器就是具有next方法的对象在调用next方法的时，
# 迭代器会返回它的下一个值，如果没有值了，则返回stopiteration。

l  = [1,2,3]    # l为可迭代对象
b = l.__iter__()  # b 为迭代器

print(next(b))
print(next(b))
print(next(b))

'''
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
StopIteration
'''


class Fibs:
    def __init__(self):
        self.a  = 0
        self.b  = 1

    def __next__(self):
        self.a,self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self

fibs = Fibs()

for f in fibs:
    if f > 1000:
        print(f)
        break