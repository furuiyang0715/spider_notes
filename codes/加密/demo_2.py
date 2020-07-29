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
    p = 'ruiyanglikeeat'
    print('明文：' + p)
    print('密文：' + Encrypt(1, p))
    print('解密：' + Decrypt(1, Encrypt(1, p)))
    assert Decrypt(1, Encrypt(1, p)) == p
