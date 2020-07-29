import base64
from Crypto.Cipher import AES


class AESCipher(object):
    def __init__(self, key):
        self.bs = 16
        key = self._pad(key)
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, raw):
        """编码"""
        raw = self._pad(raw)
        print("Input raw: ", raw)
        encrypted = self.cipher.encrypt(raw)
        print("encrypted: ", encrypted)
        return encrypted

        # encoded = base64.b64decode(encrypted)
        # print("b64 encode: ", encoded)
        # return str(encoded, 'utf-8')

    def decrypt(self, raw):
        """解码"""
        decrypted = self.cipher.decrypt(raw)
        # return str(self._unpad(decrypted), "utf-8")
        return decrypted.decode()

    def _pad(self, s):
        # 将输入进行补全
        if isinstance(s, str):
            s = s.encode()
        elif isinstance(s, bytes):
            pass
        else:
            raise ValueError("type(key) must be bytes or str.")
        # 计算与位数或者所需位数的倍数相差的位数
        # chaju = self.bs - len(s) % self.bs
        # print(chaju)
        # print(type(chr(1)))
        # print(len(chr(1)))
        padded = s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs).encode()
        # print(padded)
        # print(len(padded))
        return padded

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]


if __name__ == "__main__":
    my_key = 'ruiyanglikeseat'

    aes = AESCipher(key=my_key)

    ret = aes.encrypt("apple_happy_have".encode())
    print(ret)

    origin = aes.decrypt(ret)
    print(origin)
