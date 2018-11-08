"""
1 json反序列化
2 json.loads 就可以把json对于的字符串格式转换成python对应的数据接口  把某种数据格式转换成对应语言的一种格式我们叫反序列化
  是由字符串到我们某种语言下的
3 在python中我们确实可以用单引号来表示一个字符串 但是了在json中是和语言无关的一种格式，所以
  在json的文档中就已经告诉了大家了，必须使用双引号来表示一个字符串
4 里面是双引号那么外面就必须是单引号才能表示一个字符串格式
5 字符串转换成字典格式就是 序列化
6 在python中 json的定义个格式正好与我们python中的字典格式是一样的
7 在python中如果json格式是list[] 那么在json序列化回来就是一个数组
8 在json中布尔值是小写的false 在python中布尔值是大写的
"""
import json

a = '{"names":"bayue", "age":18}' # 这样的json字符串是不符合json的格式规范的
b = json.loads(a)
print(b)

a1 = '[{"names":"bayue", "age":18, "falge":false},{"names":"bayue", "age":18}]'  # 这样的json字符串是不符合json的格式规范的
b1 = json.loads(a1)
print(b1)








