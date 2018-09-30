"""
装饰器


"""
def deco(func):
    def in_deco(x,y):
        print('in deco')
        func(x,y)
    print('call deco')
    return in_deco  # 函数如果不显示的返回那么默认显示返回就是None
"""
deco(bar) -> in_deco
bar = in_deco
bar() in_deco bar()

"""
@deco
def bar(x,y):
    print('in bar',x+y)

bar(1,2)
