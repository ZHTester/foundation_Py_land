"""
类方法_静态方法——实例方法
1 普通法方法都是实例方法 .....  实例方法
2 静态方法 - 和我们普通的方法使用方式是一样的 静态方法的调用必须是类名+静态方法名才能进行调用，因为他已经进入了
  Data的命名空间了，静态方法最好的好处就是将命名空间变到我们的class类中来了
3 静态方法不好的地方就是，我们在return的时候采用的硬编码的方法进行编码的
4 类方法
    @classmethod
    def from_string(cls): 第一个参数传递的对象的本身也就是类实例的本身
5 类方法和实例方法 cls和无的区别
6 staticmethod的用处 我们需要判断一个字符串是否有用，我们这个时候就不需要去返回return这个类了


"""


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))

    @classmethod
    def from_string(cls,date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)


if __name__ == "__main__":
    new_day = Date(2018, 12, 31)
    new_day.tomorrow()  # tomorrow(new_day) 这样的转换的方法 self 调用的实例对象
    print(new_day)  # 这个类对象是加了打印方法的

    date_str = "2018-12-31"
    year, month, day = tuple(date_str.split("-"))
    new_day = Date(int(year), int(month), int(day))
    print(new_day)

    # 用staticmethod完成初始化  静态方法的初始化
    new_day = Date.parse_from_string(date_str)
    print(new_day)

    # 采用classmethod类方法的方式来初始化
    new_day = Date.from_string(date_str)
    print(new_day)
