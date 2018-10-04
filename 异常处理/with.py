from contextlib import contextmanager


@contextmanager
def make_myresource():
    print("《", end='')
    yield
    print("》")


# 这里的f是yield后面返回的实例
with make_myresource():
    print("my world", end='')
