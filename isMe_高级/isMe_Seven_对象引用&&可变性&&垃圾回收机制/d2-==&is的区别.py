# coding=utf-8
"""
== 和 is的区别

1 - is是判断两个对象是否相等 也就是通过id来判断 也就是判断是否是同一个对象
2 -
"""
a = 1  # a 也可以贴在int类型上面 任意的对象类型上面
a = 'abc'  # a 可以贴在字符串上面

a = [1, 2, 3]
b = a  # 所以说b和a都是贴在了同一个 类型对象上  这里也就是指向的是同一个对象
a.append(4)
print(a)
print(a is b)  # is 也就是判断是否是同一个对象

print(id(a))
print(id(b))
# --------------------------------
"""
1 python 内部有个interen机制 就是将小整数，建立一个全局的变量，然后当下次的时候，我们在使用1的时候回
然后python自动回去访问前一个变量，他不会再去生成新的变量，对于小段的字符串也是一样的道理 ~ 
2 == 为什么能判断两个值是相等的了，因为==的魔法函数就是
    def __eq__(self, *args, **kwargs): # real signature unknown
        pass
"""
# 这就是两个对象 -----> 这两个对象的id本身就不相同
a = [1, 2, 3, 4]  # 重新赋值 也就是重新生成了一个新的变量-也就是内存地址了 ---id查看值---
b = [1, 2, 3, 4]

# False
print(a is b)
# True 值是相等的，但是只是对象不是相等的 这里就会去调用list中的__eq__ 魔法函数实际上是与 ==的魔法函数相等的
print(a == b)

# --------------------------------


class People:
    pass


people = People()

if type(people) is People:
    print("yes")


