# coding=utf-8
__author__ = 'landing'
__data__ = '2019/3/2  16:56'
"""
将python对象转换成json对象
1 loads json -< python
2 dumps python-< json
3 文本文件转换成json

"""
import json


def json_to_python_file():
    f = open("./static/book.json", 'r', encoding="utf-8")
    s = f.read()
    s = json.dumps(s, indent=2, sort_keys=True)
    print(s)
    f.close()

if __name__ == "__main__":
    json_to_python_file()