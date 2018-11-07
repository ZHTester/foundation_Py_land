"""
闭包解决问题 - 也就是说闭包到底有什么作用
1 闭包只是属于函数式编程的一种 也就是属于思维方式的一种
2 含有就是面向对象的编程
问题：
非闭包的解决 旅行者行走的问题
nonlocal 强制声明不是一个本地的全局变量

闭包的关键是记忆住了上调用的状态
闭包的优势就是并没有修改全局变量 所有的操作都是基于局部变量来进行一个操作的 都是在函数的内部
函数式编程或者说闭包他不会去操作全局变量的 这就是使用函数式编程与一般编程的一个区别 与巨大的优势


"""
oragin = 0


def factiory(pos):
    def go(step):
        nonlocal pos  # 强制声明pos不是一个本地的局部变量
        new_pos = pos + step
        pos = new_pos
        return pos

    return go


tor = factiory(oragin)

print(tor(2))
print(oragin)
print(tor(4))
print(oragin)
print(tor(5))
