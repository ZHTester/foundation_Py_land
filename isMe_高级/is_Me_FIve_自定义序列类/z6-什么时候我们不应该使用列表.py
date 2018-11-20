"""
什么时候我们将使用到排序，什么时候我们不需要使用到排序

1 我们在有的时候不需要去使用list 我们可以去使用更加优化的数据结构类型
  arraylist也就是数组, array会被list的性能比较高，deque

2 array 也就是c语言中的数组，数组的存储也就是连续的内存空间，他的性能是十分高的，
  list使用c语言来写的，其中pycharm帮组我们把这些代码抽象成了python代码的形式来提供接口
  给我们看，一个函数或许他就是一个接口，也就是可以这样的来理解

3 array和list的一个重要的区别就是，array必须存放我们指定的数据类型，而list是可以存放任意的数据类型
  因为list他是一个容器，而array必须指定存放的数据类型是什么，并且我们在arry添加数据类型的时候，我们必须
  使用指定的数据类型
"""
import array

a = list
array_list = array.array("i")
array_list.append(1)
# array_list.append("c") # 这里就会报错了 因为array是指定了数据类型的
print(array_list)




