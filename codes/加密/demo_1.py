def simple_test():
    """关于加密以及解密模块的简单使用"""
    # 导入DES模块
    from Cryptodome.Cipher import DES
    import binascii

    # 这是密钥
    key = b'abcdefgh'
    # 需要去生成一个DES对象
    des = DES.new(key, DES.MODE_ECB)
    # 需要加密的数据
    text = 'python spider!'
    # 将需要加密的数据进行位数补全 差的位置都补上 "="
    text = text + (8 - (len(text) % 8)) * '='

    # 加密的过程
    encrypto_text = des.encrypt(text.encode())
    encrypto_text = binascii.b2a_hex(encrypto_text)
    print(encrypto_text)

    # 逆向解密的过程
    ret = binascii.a2b_hex(encrypto_text)
    print(ret)
    decrypto_text = des.decrypt(ret)
    print(decrypto_text)



simple_test()
