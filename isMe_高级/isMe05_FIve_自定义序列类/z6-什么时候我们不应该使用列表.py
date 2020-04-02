"""
什么时候我们将使用到排序，什么时候我们不需要使用到排序 转而去使用 - array

1 我们在有的时候不需要去使用list 我们可以去使用更加优化的数据结构类型
  arraylist也就是数组, array会比list的性能比较高，deque

2 数组在内存中是连续的存储空间, 所以数组的性能是十分的高的。

3 array 也就是c语言中的数组，数组的存储也就是连续的内存空间，他的性能是十分高的，
  当数据成量级的时候，我们就可以使用array
  list使用c语言来写的，其中pycharm帮组我们把这些代码抽象成了python代码的形式来提供接口
  给我们看，一个函数或许他就是一个接口，也就是可以这样的来理解

4 array和list的一个重要的区别就是，array必须存放我们指定的数据类型，而list是可以存放任意的数据类型
  因为list他是一个容器，而array必须指定存放的数据类型是什么，并且我们在arry添加数据类型的时候，我们必须
  使用指定的数据类型
"""
import array

a = list
# array = ArrayType（这里就是第二个array指向的就是ArrayType这个的一个class）
'''
array(typecode [, initializer]) -> array
    
    Return a new array whose items are restricted by typecode, and
    initialized from the optional initializer value, which must be a list,
    string or iterable over elements of the appropriate type.
    
    Arrays represent basic values and behave very much like lists, except
    the type of objects stored in them is constrained. The type is specified
    at object creation time by using a type code, which is a single character.
    The following type codes are defined:
    
        Type code   C Type             Minimum size in bytes 
        'b'         signed integer     1 
        'B'         unsigned integer   1 
        'u'         Unicode character  2 (see note) 
        'h'         signed integer     2 
        'H'         unsigned integer   2 
        'i'         signed integer     2 
        'I'         unsigned integer   2 
        'l'         signed integer     4 
        'L'         unsigned integer   4 
        'q'         signed integer     8 (see note) 
        'Q'         unsigned integer   8 (see note) 
        'f'         floating point     4 
        'd'         floating point     8 
    
    NOTE: The 'u' typecode corresponds to Python's unicode character. On 
    narrow builds this is 2-bytes on wide builds this is 4-bytes.
    
    NOTE: The 'q' and 'Q' type codes are only available if the platform 
    C compiler used to build Python supports 'long long', or, on Windows, 
    '__int64'.
    
    Methods:
    
    append() -- append a new item to the end of the array
    buffer_info() -- return information giving the current memory info
    byteswap() -- byteswap all the items of the array
    count() -- return number of occurrences of an object
    extend() -- extend array by appending multiple elements from an iterable
    fromfile() -- read items from a file object
    fromlist() -- append items from the list
    frombytes() -- append items from the string
    index() -- return index of first occurrence of an object
    insert() -- insert a new item into the array at a provided position
    pop() -- remove and return item (default last)
    remove() -- remove first occurrence of an object
    reverse() -- reverse the order of the items in the array
    tofile() -- write all items to a file object
    tolist() -- return the array converted to an ordinary list
    tobytes() -- return the array converted to a string
    
    Attributes:
    
    typecode -- the typecode character used to create the array
    itemsize -- the length in bytes of one array item
'''
array_list = array.array("i")
array_list.append(1)
dd = 22
array_list.append(dd)
# array_list.append("c") # 这里就会报错了 因为array是指定了数据类型的
print(array_list)
array_list.remove(dd)
print(array_list)




