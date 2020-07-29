# 关于 binascii 模块的使用
# 链接：https://www.jianshu.com/p/701960098b7a


import binascii
'''
binascii.b2a_hex(data)和binascii.hexlify(data)：返回二进制数据的十六进制表示。
每个字节被转换成相应的 2位十六进制表示形式。因此，得到的字符串是是原数据长度的两倍。 
binascii.a2b_hex(hexstr) 和binascii.unhexlify(hexstr)：从十六进制字符串hexstr返回二进制数据。
是b2a_hex的逆向操作。 hexstr必须包含偶数个十六进制数字（可以是大写或小写），否则报TypeError。

'''

# 返回二进制数据的十六进制表示
s = 'hello'.encode()
b = binascii.b2a_hex(s)
print(b)

# 将 16 进制数据转换为 二进制
ret = binascii.a2b_hex(b)
print(ret)
print(ret.decode())


# 另外一种相似的用法
b = binascii.hexlify(s)
print(b)
ret = binascii.unhexlify(b)
print(ret)
print(ret.decode())
