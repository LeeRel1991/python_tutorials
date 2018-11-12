#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: r.li
@license: Apache Licence 
@contact: r.li@bmi-tech.com
@site: 
@software: PyCharm
@file: use_super.py
@time: 18-7-6 上午9:37
@brief： 
"""

"""
TODO 知识点：
从运行结果上看，普通继承和super继承是一样的。但是其实它们的内部运行机制不一样，这一点在多重继承时体现得很明显。在super机制里可以保证公共父类仅被执行一次，至于执行的顺序，是按照mro进行的（E.__mro__）。
注意：super继承只能用于新式类，用于经典类时就会报错。
新式类：必须有继承的类，如果没什么想继承的，那就继承object
经典类：没有父类，如果此时调用super就会出现错误：『super() argument 1 must be type, not classobj』


总结
　　1. super并不是一个函数，是一个类名，形如super(B, self)事实上调用了super类的初始化函数，
       产生了一个super对象；
　　2. super类的初始化函数并没有做什么特殊的操作，只是简单记录了类类型和具体实例；
　　3. super(B, self).func的调用并不是用于调用当前类的父类的func函数；
　　4. Python的多继承类是通过mro的方式来保证各个父类的函数被逐一调用，而且保证每个父类函数
       只调用一次（如果每个类都使用super）；
　　5. 混用super类和非绑定的函数是一个危险行为，这可能导致应该调用的父类函数没有调用或者一
       个父类函数被调用多次。
"""

class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print ('Parent')

    def bar(self, message):
        print (message, 'from Parent')


class FooChild(FooParent):
    def __init__(self):
        FooParent.__init__(self)
        print ('Child')

    def bar(self, message):
        FooParent.bar(self, message)
        print ('Child bar function.')
        print (self.parent)


class FooParent1(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print(message, 'from Parent')


class FooChild1(FooParent1):
    def __init__(self):
        super(FooChild1, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild1, self).bar(message)
        print ('Child bar function.')
        print (self.parent)


"""
这个结果说明了两个问题:
1、super().add(m) 确实调用了父类 A 的 add 方法。
2、super().add(m) 调用父类方法 def add(self, m) 时, 
此时父类中 self 并不是父类的实例而是子类的实例, 所以 b.add(2) 之后的结果是 5 而不是 4 。
"""
class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super().add(m)
        self.n += 3


if __name__ == '__main__':
    print ("**********using 类名*********")
    fooChild = FooChild()
    fooChild.bar('HelloWorld')

    print ("*********using super********")
    fooChild = FooChild1()
    fooChild.bar('HelloWorld')

    print("************A B add *******")
    b = B()
    b.add(2)
    print(b.n)
