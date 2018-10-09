"""
默认参数
1 如果说我们的方法里面有几十个参数，那么我们就建议将这些参数封装成一个一个的对象
2 不能把非默认参数放到默认参数的后面 这样的语法检测是通不过的
  name, gender="中国", age=8, coolege="北京大学" teacher 这样传值的方式就是不正确的传值方式
3 关键字参数是可以不准守这样的一个形参与实际参数的一个顺序的 那么就要使用关键字的参数，因为计算机是知道你的参数是赋值给哪个参数的
4 


"""


def print_student_file(name, gender="中国", age=8, coolege="北京大学"):
    print("我叫:" + name)
    print('我今年' + str(age) + "岁")
    print('我是' + gender + "出生")
    print('我在' + coolege + "大学")


print_student_file("鸡小萌", "北京", 12, "北京大学")
print("~~~~~~~~")
print_student_file("男孩")
print("~~~~~~~~~~~")
print_student_file("北海",coolege="东京大学") # 使用关键字参数
print("~~~~~~~~~~~~")
# print_student_file("黎明",17) # 形参和实参的数据的顺序要保持一致
