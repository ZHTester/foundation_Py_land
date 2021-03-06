"""
dict和set的实现原理:
说明: 我们在什么时候使用dict什么时候使用dict 这个时候我们就需要去知道这两者的实现原理
------ 这就是dict和list中的区别  下面我们就需要知道dict和list为啥有这样的区别
    # dict查找的性能远远大于list
    # 在list中随着list数据的增大 查找时间会增大
    # 在dict中查找元素不会随着dict的增大而增大
------
1 dict 背后的实现原理是hash表也叫散列表
2 有一点很重要的，就是我们的dict中的key必须是可hash的 ，因为dict的实现原理是hash表的算法，首先我们的key会被hash函数计算出来一个值
  存档到hash表中的散列表中去，然后我们通过hash的算法，存入进去key与value ~ 但是还是有相关的特殊情况，也就是冲突
  相当于就是key c 与key b 都在计算hash值的时候，计算成相同的hash值，比如说3这个位置已经被 key b占领，那么我们现在就需要解决冲突，
  如果说是冲突了，那么他就会往前+1的形式来解决这样的冲突，这样解决冲突的方式是比较好的，因为才开始hash申请的时候就会申请一块比较小的
  内存空间~ 数组必须是连续的存储空间，才会有偏移量这样的说法，才开始申明的时候，会有较大的空白内存数组空白，这样的空白是正常的，几乎没有
  任何的hash表，能把他所有的数组都填满，hash表一定会存在浪费的，如果说当我们的hash表剩余的空间只有3分之1的时候，hash表就会重新去申请
  更加大的连续存储空间，申请完成后，他会将数据拷贝到新的空间中，如果说hash表的空间小于3分之一的时候，hash表的冲突是会更加明显的，
  所以copy新的空间，那么这样的冲突就会更加小的的 ~
3 数组和链表 最大 区别就是 数组可以做到随到随时取，通过偏移量就能很快的找到，而链表是需要从头到尾的遍历
4 如何正确的查找key a了 ~ 1 首先是计算a的散列值也叫hash值 ---- 》 2 使用散列值的一部分来定位散列值的表元(数组)
                                                                 2.1 如果是为空 那么python就会抛出一个keyerror  ，因为
                                                                     如果说有Key这个值，那么通过偏移量肯定是能找到的，但是如果
                                                                     找不到这个数据，也就是找不到这个数据，所以就会抛出keyerror
                                                                 2.2 如果表元不为空，那么我们是否就能判断数据找到了，实际上不是的
                                                                     就是在冲突的时候，我们比如说在寻找key b的时候，我们发现斌不是b,
                                                                     这个时候，我们就会采用冲突的解决方法，实际上也就是会占领以后元素的
                                                                     偏移量值，所以说如果说不为空，其实也有可能呗其他元素给占领原有的hash值
                                                                     那么我们首先是判断这个key是否相等，如果是相等那自然是没问题的
                                                                     如果这个key不相等，那么就会进一步的去计算这个散列值，然后重新来计算
                                                                     重新来这这样的一个逻辑，直到找到为止，这个就是hash查找的逻辑 ~ 为啥会这么
                                                                     快
5 dict和set都是可以hash的，所以对于我们set来说，值必须是可hash的，对我们不可变对象，都是可hash的，str int fronzenset tuple
  如果我们自己去实现了一个类，那么我们就需要去重载hash这个魔法函数，让他返回的值是可hash的，那么我们就可以把这样的值放入到dict或者set中

6 dict 内存花销大，但是查询速度快，自定义的对象 或者python内部的对象都是用dict包装的
7 dict的存储顺序和元素添加顺序有关  也就是我们首先去存储z在去存储c 那么我们读取出来的数据就是zc，这就是dict存储顺序和元素添加的顺序有关
8 添加数据有可能改变已有数据的顺序   -----> 也就说当我们的表元剩余的空间小雨三分之一的时候，hash就回去申请新的内存空间，然后把我们的旧的
  表元重新一条一条的插入到新的表元中去，所以在数据搬迁的时候，很有可能改变我们旧数据的一个位置，所以说，当我们在插入数据，造成重新分配内存的时候
  ，这就极有可能改变的。
9 set 其实和dict的性能是一样的，还有就是我们就会尽量使用set来进行去重的操作，还有就是set的内存空间是比dict小的








"""













