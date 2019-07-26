# coding=utf-8
__author__ = 'landing'
__data__ = '2019/7/23  11:14'
from flask import Flask

app = Flask(__name__)


@app.route('/')  # 路由器
def hello_word():
    return "this is my flask"


if __name__ == '__main__':
    app.run(debug=True)
