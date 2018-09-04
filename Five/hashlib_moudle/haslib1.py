"""

用于加密相关的操作，3.x里代替了md5模块和sha模块，
主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法  都是基于hash的
将字符串转换成一段固定的hash值

"""
import hashlib
# 生成一个加密的对象
m = hashlib.md5()
# 往加密对象中添加值
m.update(b"Hello")
m.update(b"It's me")
m.update('天王盖地虎 宝塔镇河妖'.encode())
print(m.digest())
m.update(b"It's been a long time since last time we ...")

print(m.digest())  # 2进制格式hash
print(len(m.hexdigest()))  # 16进制格式hash

# ######## sha1 ########

s2 = hashlib.sha1()
s2.update(b'admin')
print(s2.hexdigest())

# # ######## sha256 ########
#
ss2 = hashlib.sha256()
ss2.update(b'admin')
print(ss2.hexdigest())
#
# # ######## sha384 ########
#
s3 = hashlib.sha384()
s3.update(b'admin')
print(s3.hexdigest())
#
# # ######## sha512 ########
#
hash4 = hashlib.sha512()
hash4.update(b'admin')
print(hash4.hexdigest())






