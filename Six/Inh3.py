"""
继承实例

"""


class School(object):
    def __init__(self, name, adr):
        self.name = name
        self.adr = adr
        self.student = []
        self.staffs = []

        # 注册学员  stu_obj 学生的实例

    def enroll(self, stu_obj):
        print('为学员%s: 办理注册手续' % stu_obj.name)
        self.student.append(stu_obj)

    # 注册一个员工
    def hire(self, staff_obj):
        self.staffs.append(staff_obj)
        print('雇佣新员工%s: 办理注册手续' % staff_obj.name)


class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass


class Teacher(SchoolMember):
    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print(''' 
        ---- info  of teacher:%s ---- 
        Name: %s
        Age: %s
        Sex: %s
        Salary: %s
        course: %s
        ''' % (self.name, self.name, self.age, self.sex, self.salary, self.course))

    def teach(self):
        print('%s is teacher course[%s]' % (self.name, self.course))


class Student(SchoolMember):
    def __init__(self, name, age, sex, stu_id, grade):
        super(Student, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print(''' 
        ---- info  of Student:%s ---- 
        Name: %s
        Age: %s
        Sex: %s
        stu_id: %s
        grade: %s
        ''' % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))

    def Pay_tuition(self, amount):
        print('%s  has paid tutuon for $[%s]' % (self.name, amount))


school = School("老男孩IT", "沙河")

t1 = Teacher('oldbady', 56, 'mf', 3000000, 'Linux')
t2 = Teacher('MacHao', 2, 'm', 3000, 'Python')

s1 = Student('MacStudent', 44, 'mf', 5000, 'python')
s2 = Student('XuLiang', 19, 'm', 1003, 'python , Java')

t1.tell()
s1.tell()

school.enroll(s1)
school.hire(t1)

school.enroll(s2)
school.hire(t2)

print(school.student)
print(school.staffs)

school.staffs[0].teach()

for stu in school.student:
    print(stu.Pay_tuition(6000))
