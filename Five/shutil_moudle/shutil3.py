"""
shutil.copystat(src, dst)
拷贝状态的信息，包括：mode bits, atime, mtime, flags

"""

import shutil

shutil.copystat('shutilModule.py', 'copy1.py')

