"""
需求:
    name = CharField(db_column="", max_length=10)
    age = IntField(db_column="", max_length=100, min_length=0)
    其中CharField,IntField 采用属性描述符，来定义 name 和age的值 这里就会做一个参数的检查了


"""
import numbers


class IntField:
    def __init__(self, db_column, max_value=None, min_value=None):
        self.value = None
        self.min_value = min_value
        self.max_value = max_value
        self.db_column = db_column

        if min_value is not None:
            if isinstance(min_value, numbers.Integral):
                raise ValueError("您传入的数据需要是个整型 ~")
            elif min_value < 0:
                raise ValueError("您传入的数据必须大于0")

        if max_value is not None:
            if isinstance(max_value, numbers.Integral):
                raise ValueError("您传入的数据需要是个整型 ~")
            elif max_value < 0:
                raise ValueError("您传入的数据必须大于0")

        if max_value is not None and min_value is not None:
            if max_value < min_value:
                raise ValueError("您输入的最大数小于了最小数，输入错误，请重新输入 ~")
        else:
            pass

    # 数据属性描述符 作为参数的检查
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < self.min_value or value > self.max_value:
            raise ValueError("value must between min_value and max_value")
        self._value = value


class CharField:
    def __init__(self, db_column, max_length=None):
        self._value = None
        self.db_column = db_column
        if max_length is None:
            raise ValueError("you must spcify max_lenth for charfiled")
        self.max_length = max_length

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("string value need")
        if len(value) > self.max_length:
            raise ValueError("value len excess len of max_length")
        self._value = value


# 元类 创建对象的对象 -> 这就是对象
class moduleMeatClass(type):
    pass


"""
其中这个User,是有很多属性的,其中这个Meta也是他的属性.我们就可以使用元类 
来注入class的属性

"""


class User:
    # 我们在这里定义的是列
    name = CharField(db_column="", max_length=10)
    age = IntField(db_column="", max_value=100, min_value=0)

    # 我们在这里定义的是表名称 这里我们就使用内部的类来定义这些类型属性
    # 在Django中我们不定义这个Meta，那么Django默认就是使用class小写的名称
    class Meta:
        db_table = "user"


if __name__ == "__main__":
    user = User()
    user.age = 30
    user.name = "landing"
    user.save()

