"""
闭包解决问题 - 也就是说闭包到底有什么作用
1 闭包只是属于函数式编程的一种 也就是属于思维方式的一种
2 含有就是面向对象的编程
问题：
非闭包的解决 旅行者行走的问题

"""

origin = 0


def go(step):
    global origin
    new_pos = origin + step  # 这个origin 是没有定义那么就会报错的
    origin = new_pos  # python会认为你左边的origin是局部变量就不会再去查找全局变量了
    return origin

# 在这里是修改了全局变量的值 因为全局变量是暴露在外面的
print(go(2))
print(origin)
print(go(3))
print(origin)
print(go(4))
