"""
浅copy


"""
import copy
person = ["TaiGuLi",["a,100"]]
"""
# 这三种实现的都是浅Copy
p1 =copy.copy(person)
p2 = person[:]
p3 = list(person)

print(p1,p2,p3)  # 上面三种方式实现的都是浅copy
"""
p1 = person[:]
p2 = person[:]

p1[0] = "bei"
p2[0] = "quan"

p1[1][1] = 50  # 联合账号

print(p1)
print(p2)



















































