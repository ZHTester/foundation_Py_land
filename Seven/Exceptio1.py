"""
1 异常处理
  虽然程序出错了但是不想让用户看到
2 统一处理相同的错误方式
"""
name = ['mac hao', 'mac chen']
data = {}
try:
    # name[3]
    # data['name']
    open('text.txt')
    name[1]
    # a = 1
    # print(a)
except (KeyError, IndexError) as e:
    print('没有这个key', e)
except IndexError as e:
    print('列表操作错误', e)
except Exception as e:
    print('未知错误')
except BaseException as e:
    print('Exception 是BaseException 未知错误')

else:
    print('一切正常')

finally:
    print('不管有错没错都继续执行')























