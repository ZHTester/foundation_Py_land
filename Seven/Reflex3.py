"""
反射
hasattr(obj, name_str) 判断一个对象obj里是否有对应的name_str字符串的方法映射
getattr(obj,name_str) 根据字符串去获取obj对象里的对应方法的内存地址
setattr(obj,y,z) 通过字符串设置新的字符串新的属性

"""
def bulk(self):
    print('%s is yelling....' % self.name)

class Dog(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('%s is eating.....' % self.name, food)




d = Dog(' niuhanyang')
choice = input('>>>:').strip()

# 反射删除

if (hasattr(d, choice)):
    delattr(d,choice)
else:
    setattr(d, choice, bulk)  # 动态装配一个方法
    print(getattr(d,choice))
print(d.name)



