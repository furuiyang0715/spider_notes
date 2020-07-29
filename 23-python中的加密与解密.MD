### ascii 
```python
def get_ascii():
    for c in "furuiyang":
        print(ord(c))
    print()
    for word in "沸羊羊":
        print(ord(word))


def get_char():
    asc_codes = [ord(c) for c in "happy"]
    for asc_code in asc_codes:
        print(chr(asc_code), end=',')


get_ascii()
get_char()
```

## md5 
```python
def get_word_md5():
    """对字符串进行 hash """
    hm = hashlib.md5()
    # 进行 md5 的字符必须是 bytes 类型的
    hm.update("ruiyang".encode())
    print(hm.hexdigest())


def get_file_mds():
    """对文件进行 hash """
    hash_md5 = hashlib.md5()
    with open("./test.txt", "rb") as f:
        # 每次读取 10 字节的 bytes
        # 每次读取的大小不对最终的  hash 结果造成影响
        for chunk in iter(lambda: f.read(10), b""):
            hash_md5.update(chunk)
    print(hash_md5.hexdigest())


get_word_md5()
get_file_mds()
```

## 什么是对称加密 
对称加密的意思是加密和解密的秘钥是一样的。 
下面简单使用字母表移位的方式进行对称的加密和解密： 
```python
# 使用字母表移位的方式进行简单的加密以及解密 
def _move_leter(letter, n):
    """
    把字母变为字母表后n位的字母,z后面接a
    :param letter: 小写字母
    :param n: 要移动的字母
    :return: 移动的结果
    """
    _first = ord("a")
    _instance = ord(letter) - _first
    _new_instance = (_instance + n) % 26
    _new_char = chr(_new_instance + _first)
    return _new_char

    # return chr((ord(letter) - ord('a') + n) % 26 + ord('a'))


def Encrypt(k, p):
    """
    移位密码加密函数E
    :param k: 秘钥k,每个字母在字母表中移动k位
    :param p: 明文p
    :return: 密文c
    """
    letter_list = list(p.lower())
    c = ''.join([_move_leter(x, k) for x in letter_list])
    return c


def Decrypt(k, c):
    """
    移位密码解密函数D
    :param k: 秘钥k,每个字母在字母表中移动k位
    :param c: 密文c
    :return: 明文p
    """
    letter_list = list(c.lower())
    p = ''.join([_move_leter(x, -k) for x in letter_list])
    return p


if __name__ == '__main__':
    p = 'ilovecoding'
    print('明文：' + p)
    print('密文：' + Encrypt(1, p))
    print('解密：' + Decrypt(1, Encrypt(1, p)))
    assert Decrypt(1, Encrypt(1, p)) == p
```
## 关于 Python 的加密库 
Pycrypto 是 python 实现的密码方面的最有名的第三方软件包，提供了许多加密算法。 
遗憾的是，它的开发工作在 2012 年就已经停止。 
幸运的是，有一个该项目的分支PyCrytodome 取代了 PyCrypto. 
### 安装 
```shell script
pip install pycrypto
pip install pycryptodomex 
```

### 导入 
```python
import Crypto  
import Cryptodome   # 在 win 中的导入 
```

### 实现简单的 aes 加密解密 
```python
import sys
from binascii import b2a_hex, a2b_hex

from Crypto import Random
from Crypto.Cipher import AES


class AesEncryption(object):
    def __init__(self, key, mode=AES.MODE_CFB):
        self.key = self.check_key(key)
        # 密钥 key 长度必须为16,24或者32bytes的长度
        self.mode = mode
        self.iv = Random.new().read(AES.block_size)

    def check_key(self, key):
        """
        检测 key 的长度是否为 16,24 或者 32bytes 的长度
        :param key:
        :return:
        """
        try:
            if isinstance(key, bytes):
                assert len(key) in [16, 24, 32]
                return key
            elif isinstance(key, str):
                assert len(key.encode()) in [16, 24, 32]
                return key.encode()
            else:
                raise Exception(f'密钥必须为str或bytes,不能为{type(key)}')
        except AssertionError:
            print('输入的长度不正确')

    def check_data(self, data):
        """
        检测进行加密的数据类型
        :param data:
        :return:
        """
        if isinstance(data, str):
            data = data.encode()
        elif isinstance(data, bytes):
            pass
        else:
            raise Exception(f'加密的数据必须为str或bytes,不能为{type(data)}')
        return data

    def encrypt(self, data):
        """
        加密
        :param data:
        :return:
        """
        data = self.check_data(data)
        cryptor = AES.new(self.key, self.mode, self.iv)
        return b2a_hex(cryptor.encrypt(data)).decode()

    def decrypt(self, data):
        """
        解密
        :param data:
        :return:
        """
        data = self.check_data(data)
        cryptor = AES.new(self.key, self.mode, self.iv)
        return cryptor.decrypt(a2b_hex(data)).decode()


if __name__ == '__main__':
    key = b'a' * 16
    data = '你真帅'
    aes = AesEncryption(key)
    e = aes.encrypt(data)  # 调用加密函数
    d = aes.decrypt(e)  # 调用解密函数
    print(e)
    print(d)
```


## 参考文章 
https://segmentfault.com/a/1190000014666335
https://www.jianshu.com/p/4ba20afacce2 
